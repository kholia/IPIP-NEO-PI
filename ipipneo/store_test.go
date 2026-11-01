package main

import (
	"io/ioutil"
	"os"
	"path/filepath"
	"strings"
	"testing"
)

func TestStoreUpgradesOldHeader(t *testing.T) {
	dir, err := ioutil.TempDir("", "ipipneo")
	if err != nil {
		t.Fatal(err)
	}
	defer os.RemoveAll(dir)
	path := filepath.Join(dir, "results.csv")
	old := utf8BOM + oldCSVHeader + "\r\n2026-10-01 10:00:00.000000,Male,30,old,India,3 3 3\r\n"
	if err := ioutil.WriteFile(path, []byte(old), 0644); err != nil {
		t.Fatal(err)
	}

	store, err := OpenStore(path)
	if err != nil {
		t.Fatal(err)
	}
	sub := &Submission{Sex: "Intersex", Gender: "Other", OtherGender: "=cmd", Age: 40, Nick: "new", Country: "USA"}
	if err := store.Save(sub); err != nil {
		t.Fatal(err)
	}
	rows, err := store.Rows()
	if err != nil {
		t.Fatal(err)
	}
	if got := strings.Join(rows[0], ","); got != strings.Join(csvHeader, ",") {
		t.Errorf("header = %q", got)
	}
	if len(rows) != 3 || rows[1][3] != "old" || rows[2][1] != "Intersex" || rows[2][6] != "Other" {
		t.Fatalf("rows = %q", rows)
	}
	if rows[2][7] != "'=cmd" {
		t.Errorf("formula not neutralized: %q", rows[2][7])
	}

	// Opening an up-to-date file must not change it.
	before, _ := ioutil.ReadFile(path)
	if _, err := OpenStore(path); err != nil {
		t.Fatal(err)
	}
	after, _ := ioutil.ReadFile(path)
	if string(before) != string(after) {
		t.Error("OpenStore modified an up-to-date file")
	}
}

func TestStoreNewFile(t *testing.T) {
	dir, err := ioutil.TempDir("", "ipipneo")
	if err != nil {
		t.Fatal(err)
	}
	defer os.RemoveAll(dir)
	store, err := OpenStore(filepath.Join(dir, "sub", "results.csv"))
	if err != nil {
		t.Fatal(err)
	}
	if err := store.Save(&Submission{Sex: "Female", Gender: "Female", Age: 25}); err != nil {
		t.Fatal(err)
	}
	data, _ := ioutil.ReadFile(store.Path)
	if !strings.HasPrefix(string(data), utf8BOM+strings.Join(csvHeader, ",")+"\r\n") {
		t.Errorf("unexpected file start: %q", data[:60])
	}
}

func TestEvaluateReference(t *testing.T) {
	// tests/reference.dat from the 2021 Python version: a 28-year-old man,
	// whose official EXTRAVERSION graph read 76, 82, 64, 63, 88, 26, 84.
	answers := "455454245414355144252442444444435454354214445435053442424254" +
		"455453415314242354554251515543245452445414245444452135425154"
	var q [items]int
	for i, c := range answers {
		q[i+1] = int(c - '0')
	}
	r, err := Evaluate("Male", 28, "user", "India", q)
	if err != nil {
		t.Fatal(err)
	}
	got := []int{r.SEP, r.SEFP[1], r.SEFP[2], r.SEFP[3], r.SEFP[4], r.SEFP[5], r.SEFP[6]}
	want := []int{76, 82, 64, 63, 88, 26, 84}
	for i := range want {
		if got[i] != want[i] {
			t.Fatalf("EXTRAVERSION scores = %v, want %v", got, want)
		}
	}
}
