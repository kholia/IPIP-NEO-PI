//go:build ignore
// +build ignore

// mkzip writes a ZIP archive with fixed timestamps, so release ZIPs are
// reproducible.
//
// Usage: go run mkzip.go <output.zip> <folder in zip> <file>...
package main

import (
	"archive/zip"
	"io/ioutil"
	"log"
	"os"
	"path/filepath"
	"time"
)

func main() {
	if len(os.Args) < 4 {
		log.Fatal("usage: go run mkzip.go <output.zip> <folder in zip> <file>...")
	}
	f, err := os.Create(os.Args[1])
	if err != nil {
		log.Fatal(err)
	}
	zw := zip.NewWriter(f)
	stamp := time.Date(2021, 6, 1, 0, 0, 0, 0, time.UTC)
	for _, name := range os.Args[3:] {
		data, err := ioutil.ReadFile(name)
		if err != nil {
			log.Fatal(err)
		}
		hdr := &zip.FileHeader{Name: os.Args[2] + "/" + filepath.Base(name), Method: zip.Deflate}
		hdr.Modified = stamp
		hdr.SetMode(0755)
		w, err := zw.CreateHeader(hdr)
		if err != nil {
			log.Fatal(err)
		}
		if _, err := w.Write(data); err != nil {
			log.Fatal(err)
		}
	}
	if err := zw.Close(); err != nil {
		log.Fatal(err)
	}
	if err := f.Close(); err != nil {
		log.Fatal(err)
	}
}
