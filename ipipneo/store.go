package main

// Results storage: an append-only CSV file. The first six columns match the
// RESULTS table of the old SQLite results.db (whose "Gender" column held the
// sex). CSV needs no cgo (there is no pure-Go SQLite for Go 1.10) and opens
// directly in Excel / LibreOffice.

import (
	"bytes"
	"encoding/csv"
	"fmt"
	"io/ioutil"
	"os"
	"path/filepath"
	"strconv"
	"strings"
	"sync"
	"time"
)

var csvHeader = []string{"Timestamp", "Sex", "Age", "Nick", "Country", "Responses", "GenderIdentity", "OtherGenderIdentity"}

// Header written by versions before the gender identity question was added.
const oldCSVHeader = "Timestamp,Gender,Age,Nick,Country,Responses"

// utf8BOM makes Excel detect the file as UTF-8.
const utf8BOM = "\xef\xbb\xbf"

type Store struct {
	Path string
	mu   sync.Mutex
}

// OpenStore picks the results file: the given path, else results.csv next to
// the executable, else (when that folder is read-only, e.g. Program Files)
// %APPDATA%\IPIP-NEO-PI\results.csv.
func OpenStore(path string) (*Store, error) {
	var candidates []string
	if path != "" {
		candidates = append(candidates, path)
	} else {
		if exe, err := os.Executable(); err == nil {
			if exe, err = filepath.EvalSymlinks(exe); err == nil {
				candidates = append(candidates, filepath.Join(filepath.Dir(exe), "results.csv"))
			}
		}
		if appdata := os.Getenv("APPDATA"); appdata != "" {
			candidates = append(candidates, filepath.Join(appdata, "IPIP-NEO-PI", "results.csv"))
		}
		candidates = append(candidates, "results.csv")
	}

	var lastErr error
	for _, p := range candidates {
		if err := os.MkdirAll(filepath.Dir(p), 0755); err != nil {
			lastErr = err
			continue
		}
		f, err := os.OpenFile(p, os.O_WRONLY|os.O_APPEND|os.O_CREATE, 0644)
		if err != nil {
			lastErr = err
			continue
		}
		f.Close()
		if err := upgradeHeader(p); err != nil {
			return nil, err
		}
		return &Store{Path: p}, nil
	}
	return nil, fmt.Errorf("cannot create a results file: %v", lastErr)
}

// upgradeHeader rewrites an old-style header line in place; old rows stay
// valid as they have the same first six columns.
func upgradeHeader(path string) error {
	data, err := ioutil.ReadFile(path)
	if err != nil {
		return err
	}
	body := bytes.TrimPrefix(data, []byte(utf8BOM))
	nl := bytes.IndexByte(body, '\n')
	if nl < 0 || strings.TrimRight(string(body[:nl]), "\r") != oldCSVHeader {
		return nil
	}
	var buf bytes.Buffer
	buf.WriteString(utf8BOM + strings.Join(csvHeader, ",") + "\r\n")
	buf.Write(body[nl+1:])
	tmp := path + ".tmp"
	if err := ioutil.WriteFile(tmp, buf.Bytes(), 0644); err != nil {
		return err
	}
	return os.Rename(tmp, path)
}

// csvSafe stops spreadsheet apps from treating free-text fields as formulas.
func csvSafe(s string) string {
	if s != "" && strings.ContainsAny(s[:1], "=+-@\t\r") {
		return "'" + s
	}
	return s
}

func (s *Store) Save(r *Submission) error {
	responses := make([]string, 0, items-1)
	for i := 1; i < items; i++ {
		responses = append(responses, strconv.Itoa(r.Q[i]))
	}
	row := []string{
		time.Now().Format("2006-01-02 15:04:05.000000"),
		r.Sex,
		strconv.Itoa(r.Age),
		csvSafe(r.Nick),
		csvSafe(r.Country),
		strings.Join(responses, " "),
		r.Gender,
		csvSafe(r.OtherGender),
	}

	s.mu.Lock()
	defer s.mu.Unlock()

	f, err := os.OpenFile(s.Path, os.O_WRONLY|os.O_APPEND|os.O_CREATE, 0644)
	if err != nil {
		return err
	}
	fi, err := f.Stat()
	if err != nil {
		f.Close()
		return err
	}
	var buf bytes.Buffer
	if fi.Size() == 0 {
		buf.WriteString(utf8BOM)
	}
	w := csv.NewWriter(&buf)
	w.UseCRLF = true
	if fi.Size() == 0 {
		w.Write(csvHeader)
	}
	w.Write(row)
	w.Flush()
	if _, err := f.Write(buf.Bytes()); err != nil {
		f.Close()
		return err
	}
	return f.Close()
}

// Rows returns all saved rows, header included.
func (s *Store) Rows() ([][]string, error) {
	s.mu.Lock()
	data, err := ioutil.ReadFile(s.Path)
	s.mu.Unlock()
	if os.IsNotExist(err) {
		return nil, nil
	}
	if err != nil {
		return nil, err
	}
	r := csv.NewReader(bytes.NewReader(bytes.TrimPrefix(data, []byte(utf8BOM))))
	r.FieldsPerRecord = -1
	return r.ReadAll()
}
