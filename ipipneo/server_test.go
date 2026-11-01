package main

import (
	"io/ioutil"
	"math/rand"
	"net/http"
	"net/http/httptest"
	"net/url"
	"os"
	"path/filepath"
	"strconv"
	"strings"
	"testing"
)

func testServer(t *testing.T) (*httptest.Server, func()) {
	if err := loadTemplates(); err != nil {
		t.Fatal(err)
	}
	dir, err := ioutil.TempDir("", "ipipneo")
	if err != nil {
		t.Fatal(err)
	}
	store, err := OpenStore(filepath.Join(dir, "results.csv"))
	if err != nil {
		t.Fatal(err)
	}
	// Without recoverPanics, so a panic fails the test instead of being hidden.
	srv := httptest.NewServer(newMux(store))
	return srv, func() { srv.Close(); os.RemoveAll(dir) }
}

var nastyValues = []string{
	"", " ", "0", "-1", "1", "2", "3", "5", "6", "9", "10", "99", "100",
	"9999999999999999999999", "-9223372036854775808", "9223372036854775807",
	"1e309", "NaN", "Inf", "0x10", " 28 ", "28abc", "Male", "Female", "Intersex",
	"male", "=1+1", "<script>alert(1)</script>", "\x00", "\xff\xfe", "日本語",
	strings.Repeat("A", 100000), "%", "&", "\"'", "{{.Nick}}",
}

var fields = []string{"Accuracy", "Sex", "Gender", "OtherGender", "Age", "Nick", "Country"}

// TestNoPanicsOrServerErrors posts random garbage to every route; the server
// must always answer, and never with a 5xx status.
func TestNoPanicsOrServerErrors(t *testing.T) {
	srv, cleanup := testServer(t)
	defer cleanup()

	rng := rand.New(rand.NewSource(1))
	pick := func() string { return nastyValues[rng.Intn(len(nastyValues))] }
	routes := []string{"/", "/shortipipneo", "/results", "/results_api", "/reporting",
		"/results.csv", "/ping", "/css/site.css", "/js/../../etc/passwd", "/nope",
		"/%2e%2e/%2e%2e/", "//results", "/static/css/site.css"}

	for i := 0; i < 1500; i++ {
		form := url.Values{}
		for _, f := range fields {
			if rng.Intn(4) > 0 {
				form.Set(f, pick())
			}
		}
		if rng.Intn(3) == 0 { // a mostly-valid submission
			form.Set("Sex", strconv.Itoa(1+rng.Intn(3)))
			form.Set("Gender", strconv.Itoa(1+rng.Intn(9)))
			form.Set("Age", strconv.Itoa(rng.Intn(120)))
		}
		for q := 0; q <= 121; q++ {
			switch rng.Intn(4) {
			case 0:
			case 1:
				form.Add("Q"+strconv.Itoa(q), pick())
			default:
				form.Set("Q"+strconv.Itoa(q), strconv.Itoa(1+rng.Intn(5)))
			}
		}
		route := routes[rng.Intn(len(routes))]
		var resp *http.Response
		var err error
		if rng.Intn(4) == 0 {
			resp, err = http.Get(srv.URL + route + "?" + form.Encode())
		} else {
			resp, err = http.PostForm(srv.URL+route, form)
		}
		if err != nil {
			t.Fatalf("%s: no response (server panicked?): %v", route, err)
		}
		ioutil.ReadAll(resp.Body)
		resp.Body.Close()
		if resp.StatusCode >= 500 {
			t.Fatalf("%s: status %d for form %v", route, resp.StatusCode, form)
		}
	}
}

func TestRecoverPanics(t *testing.T) {
	h := recoverPanics(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		panic("boom")
	}))
	rec := httptest.NewRecorder()
	h.ServeHTTP(rec, httptest.NewRequest("GET", "/", nil))
	if rec.Code != http.StatusInternalServerError {
		t.Errorf("status = %d, want 500", rec.Code)
	}
}
