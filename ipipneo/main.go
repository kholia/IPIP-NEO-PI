// IPIP-NEO-PI: self-contained, offline web app for the IPIP-NEO-120 test.
//
// This file must keep building with Go 1.10.8 (the last Go release that runs
// on Windows XP), so stick to the standard library and APIs available there.
package main

import (
	"bytes"
	"flag"
	"fmt"
	"html/template"
	"io/ioutil"
	"log"
	"net"
	"net/http"
	"os"
	"os/exec"
	"path"
	"runtime"
	"strconv"
	"strings"
	"time"
)

var version = "dev" // set with -ldflags "-X main.version=..."

const pingBody = "IPIP-NEO-PI"

// formError is a user-facing validation failure, shown as its own page like
// the official site does.
type formError struct{ title, message string }

var (
	errAccuracy = &formError{"Failure to Acknowledge Purpose and Limitations",
		`You did not indicate you understand the purpose and limitations of this on-line
		inventory. To access the inventory you must return to the previous page and click the
		box indicating your understanding of the purpose and limitations of the IPIP-NEO`}

	errSex = &formError{"Failure to Indicate Sex Assigned at Birth",
		`You did not indicate your sex assigned at birth at the beginning of the inventory.
		You cannot complete this personality inventory unless you indicate whether your sex
		assigned at birth was male, female, or intersex. Please return to the inventory and
		indicate your sex.`}

	errGender = &formError{"Failure to Indicate Gender Identity",
		`You did not indicate your gender identity at the beginning of the inventory. You
		cannot complete this personality inventory unless you indicate your gender identity.
		Note that this information is gathered only to improve future versions of this
		inventory. It has no bearing on your current results. Please return to the inventory
		and indicate your gender identity.`}

	errAge = &formError{"Failure to Indicate Age",
		`You did not indicate how old you are at the beginning of the inventory, or you typed
		in an age that is too young. Your answers cannot be normed properly unless type in a
		valid age. Please return to the inventory and change your response.`}

	errIntersex = &formError{"Report Not Yet Available",
		`Thank you for completing the inventory. Your responses have been saved. This offline
		version of the inventory cannot yet produce a report for respondents whose sex assigned
		at birth is intersex: it still uses the norms of the 2021 version of the online
		inventory, which are separate for males and females.`}
)

// The official form sends numeric codes; "Male"/"Female" are accepted too,
// for the 2021 form and /results_api clients.
var sexCodes = map[string]string{
	"1": "Male", "2": "Female", "3": "Intersex",
	"Male": "Male", "Female": "Female", "Intersex": "Intersex",
}

var genderCodes = map[string]string{
	"1": "Male", "2": "Female", "3": "Nonbinary", "4": "Gender Fluid",
	"5": "Gender Queer", "6": "Gender Neutral", "7": "Questioning/Exploring",
	"8": "Prefer not to answer", "9": "Other",
}

// Submission is one completed inventory.
type Submission struct {
	Sex, Gender, OtherGender, Nick, Country string
	Age                                     int
	Q                                       [items]int
}

var pages = map[string]*template.Template{}

func loadTemplates() error {
	base, err := template.New("base").Parse(assets["views/base.html"])
	if err != nil {
		return err
	}
	for _, name := range []string{"index", "shortipipneo", "results", "reporting", "message"} {
		src, ok := assets["views/"+name+".html"]
		if !ok {
			return fmt.Errorf("missing embedded template %s", name)
		}
		t, err := base.Clone()
		if err == nil {
			_, err = t.Parse(src)
		}
		if err != nil {
			return fmt.Errorf("template %s: %v", name, err)
		}
		pages[name] = t
	}
	return nil
}

func render(w http.ResponseWriter, name string, data interface{}) {
	t, ok := pages[name]
	if !ok {
		log.Printf("unknown template %s", name)
		http.Error(w, "internal error", http.StatusInternalServerError)
		return
	}
	var buf bytes.Buffer
	if err := t.ExecuteTemplate(&buf, "base", data); err != nil {
		log.Printf("template %s: %v", name, err)
		http.Error(w, "internal error", http.StatusInternalServerError)
		return
	}
	w.Header().Set("Content-Type", "text/html; charset=utf-8")
	w.Write(buf.Bytes())
}

func renderError(w http.ResponseWriter, e *formError) {
	render(w, "message", map[string]string{"title": e.title, "message": e.message})
}

// parseForm extracts and validates a submitted inventory.
func parseForm(w http.ResponseWriter, r *http.Request, requireGender bool) (*Submission, *formError) {
	r.Body = http.MaxBytesReader(w, r.Body, 1<<20)
	if err := r.ParseForm(); err != nil {
		return nil, &formError{"Invalid Form", "Invalid form submission."}
	}
	f := r.PostForm
	sub := &Submission{
		Sex:         sexCodes[f.Get("Sex")],
		Gender:      genderCodes[f.Get("Gender")],
		OtherGender: strings.TrimSpace(f.Get("OtherGender")),
		Nick:        f.Get("Nick"),
		Country:     f.Get("Country"),
	}
	if sub.Sex == "" {
		return nil, errSex
	}
	if requireGender && sub.Gender == "" {
		return nil, errGender
	}
	if sub.Gender != "Other" {
		sub.OtherGender = ""
	}
	var err error
	sub.Age, err = strconv.Atoi(strings.TrimSpace(f.Get("Age")))
	if err != nil || sub.Age < 10 {
		return nil, errAge
	}
	for i := 1; i < items; i++ {
		sub.Q[i], _ = strconv.Atoi(f.Get("Q" + strconv.Itoa(i)))
	}
	return sub, nil
}

func handleItems(w http.ResponseWriter, r *http.Request) {
	if r.FormValue("Accuracy") != "Yes" {
		renderError(w, errAccuracy)
		return
	}
	render(w, "shortipipneo", nil)
}

func handleResults(store *Store) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		if r.Method != "POST" {
			http.Redirect(w, r, "/", http.StatusSeeOther)
			return
		}
		sub, ferr := parseForm(w, r, true)
		if ferr != nil {
			renderError(w, ferr)
			return
		}
		if err := store.Save(sub); err != nil {
			log.Printf("saving results: %v", err)
		}
		if sub.Sex == "Intersex" {
			renderError(w, errIntersex)
			return
		}
		res, err := Evaluate(sub.Sex, sub.Age, sub.Nick, sub.Country, sub.Q)
		if err != nil {
			log.Printf("scoring: %v", err)
			http.Error(w, "internal error", http.StatusInternalServerError)
			return
		}
		render(w, "results", map[string]interface{}{
			"Nick": res.Nick, "Country": res.Country, "Category": res.Category,
			"LO": lo, "HI": hi,
			"SN": res.SN, "SE": res.SE, "SO": res.SO, "SA": res.SA, "SC": res.SC,
			"SNP": res.SNP, "SEP": res.SEP, "SOP": res.SOP, "SAP": res.SAP, "SCP": res.SCP,
			"SNFP": res.SNFP, "SEFP": res.SEFP, "SOFP": res.SOFP, "SAFP": res.SAFP, "SCFP": res.SCFP,
			"flev": res.Flev,
		})
	}
}

func handleResultsAPI(w http.ResponseWriter, r *http.Request) {
	if r.Method != "POST" {
		http.Error(w, "POST required", http.StatusMethodNotAllowed)
		return
	}
	sub, ferr := parseForm(w, r, false)
	if ferr == nil && sub.Sex == "Intersex" {
		ferr = errIntersex
	}
	if ferr != nil {
		http.Error(w, ferr.message, http.StatusBadRequest)
		return
	}
	res, err := Evaluate(sub.Sex, sub.Age, sub.Nick, sub.Country, sub.Q)
	if err != nil {
		log.Printf("scoring: %v", err)
		http.Error(w, "internal error", http.StatusInternalServerError)
		return
	}
	w.Header().Set("Content-Type", "application/json")
	w.Write(res.JSON())
}

func handleReporting(store *Store) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		rows, err := store.Rows()
		if err != nil {
			log.Printf("reading results: %v", err)
			http.Error(w, "could not read "+store.Path, http.StatusInternalServerError)
			return
		}
		render(w, "reporting", map[string]interface{}{"rows": rows, "path": store.Path})
	}
}

func handleCSV(store *Store) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		data, err := ioutil.ReadFile(store.Path)
		if err != nil && !os.IsNotExist(err) {
			http.Error(w, "could not read "+store.Path, http.StatusInternalServerError)
			return
		}
		w.Header().Set("Content-Type", "text/csv; charset=utf-8")
		w.Header().Set("Content-Disposition", `attachment; filename="results.csv"`)
		w.Write(data)
	}
}

var contentTypes = map[string]string{
	".css":   "text/css; charset=utf-8",
	".js":    "application/javascript",
	".ico":   "image/x-icon",
	".png":   "image/png",
	".gif":   "image/gif",
	".jpg":   "image/jpeg",
	".svg":   "image/svg+xml",
	".eot":   "application/vnd.ms-fontobject",
	".ttf":   "font/ttf",
	".woff":  "font/woff",
	".woff2": "font/woff2",
}

// handleStatic serves embedded files from app/static.
func handleStatic(w http.ResponseWriter, r *http.Request) {
	name := path.Clean(r.URL.Path)
	data, ok := assets["static"+name]
	if !ok {
		http.NotFound(w, r)
		return
	}
	if ct, ok := contentTypes[path.Ext(name)]; ok {
		w.Header().Set("Content-Type", ct)
	}
	w.Header().Set("Cache-Control", "max-age=3600")
	w.Write([]byte(data))
}

// recoverPanics answers any request whose handler panics with a 500 page
// instead of dropping the connection. Handlers should never panic; this is
// only a safety net.
func recoverPanics(h http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		defer func() {
			if err := recover(); err != nil {
				log.Printf("BUG: panic serving %s: %v", r.URL.Path, err)
				http.Error(w, "internal error", http.StatusInternalServerError)
			}
		}()
		h.ServeHTTP(w, r)
	})
}

func newHandler(store *Store) http.Handler {
	return recoverPanics(newMux(store))
}

func newMux(store *Store) *http.ServeMux {
	mux := http.NewServeMux()
	mux.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		if r.URL.Path != "/" {
			handleStatic(w, r)
			return
		}
		render(w, "index", nil)
	})
	mux.HandleFunc("/shortipipneo", handleItems)
	mux.HandleFunc("/results", handleResults(store))
	mux.HandleFunc("/results_api", handleResultsAPI)
	mux.HandleFunc("/reporting", handleReporting(store))
	mux.HandleFunc("/results.csv", handleCSV(store))
	mux.HandleFunc("/ping", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprint(w, pingBody)
	})
	return mux
}

// alreadyRunning reports whether another copy of this app owns addr.
func alreadyRunning(addr string) bool {
	c := http.Client{Timeout: 2 * time.Second}
	resp, err := c.Get("http://" + addr + "/ping")
	if err != nil {
		return false
	}
	defer resp.Body.Close()
	body, _ := ioutil.ReadAll(resp.Body)
	return string(body) == pingBody
}

func openBrowser(url string) {
	var cmd *exec.Cmd
	switch runtime.GOOS {
	case "windows":
		// Works on everything from Windows XP to Windows 11.
		cmd = exec.Command("rundll32", "url.dll,FileProtocolHandler", url)
	case "darwin":
		cmd = exec.Command("open", url)
	default:
		cmd = exec.Command("xdg-open", url)
	}
	if err := cmd.Start(); err != nil {
		log.Printf("could not open a web browser (%v); please open %s manually", err, url)
	}
}

// pause keeps the console window open on Windows so errors can be read.
func pause() {
	if runtime.GOOS == "windows" {
		fmt.Println("\nPress Enter to close this window.")
		fmt.Scanln()
	}
}

func main() {
	port := flag.Int("port", 8888, "TCP port to listen on (localhost only)")
	noBrowser := flag.Bool("no-browser", false, "do not open a web browser")
	dataFile := flag.String("data", "", "results CSV file (default: results.csv next to the program)")
	flag.Parse()

	fmt.Printf("IPIP-NEO-PI %s\n\n", version)
	if err := loadTemplates(); err != nil {
		fmt.Printf("ERROR: %v\n", err)
		pause()
		os.Exit(1)
	}

	store, err := OpenStore(*dataFile)
	if err != nil {
		fmt.Printf("ERROR: %v\n", err)
		pause()
		os.Exit(1)
	}

	addr := "127.0.0.1:" + strconv.Itoa(*port)
	ln, err := net.Listen("tcp", addr)
	if err != nil {
		if alreadyRunning(addr) {
			fmt.Println("IPIP-NEO-PI is already running; opening it in your web browser.")
			if !*noBrowser {
				openBrowser("http://" + addr + "/")
			}
			time.Sleep(3 * time.Second)
			return
		}
		fmt.Printf("ERROR: cannot listen on %s: %v\n", addr, err)
		fmt.Println("Another program is using this port. Try running with -port 8899")
		pause()
		os.Exit(1)
	}

	url := "http://" + addr + "/"
	fmt.Printf("Test is running at:    %s\n", url)
	fmt.Printf("Past results:          %sreporting\n", url)
	fmt.Printf("Results are saved to:  %s\n\n", store.Path)
	fmt.Println("Keep this window open while taking the test. Close it to stop.")

	if !*noBrowser {
		openBrowser(url)
	}
	srv := &http.Server{Handler: newHandler(store), ReadTimeout: time.Minute, WriteTimeout: time.Minute}
	err = srv.Serve(ln)
	fmt.Printf("ERROR: server stopped: %v\n", err)
	pause()
	os.Exit(1)
}
