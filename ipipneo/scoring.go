package main

// Personality scoring logic, ported line-for-line from app/evaluator.py
// (shortipipneo3.cgi from IPIPlinux.zip, June 2021).

import (
	"bytes"
	"fmt"
	"math"
)

const (
	items = 121 // shortipipneo: Q1..Q120

	maxInt = int(^uint(0) >> 1)

	// Cubic approximations for percentiles
	const1 = 210.335958661391
	const2 = 16.7379362643389
	const3 = 0.405936512733332
	const4 = 0.00270624341822222

	lo = 45.0
	hi = 55.0
)

type normTable struct {
	sex      string
	maxAge   int // inclusive upper bound of the age bracket
	category string
	norm     [71]float64
}

var norms = []normTable{
	{"Male", 20, "males less than 21 years of age", [71]float64{
		0, 67.84, 80.70, 85.98, 81.98, 79.66, 15.83, 15.37, 12.37, 14.66, 14.49,
		11.72, 11.93, 10.58, 12.38, 11.67, 9.63, 3.76, 4.41, 4.25, 3.83, 3.25,
		3.38, 13.76, 12.23, 14.06, 11.54, 14.67, 14.41, 3.78, 4.17, 3.66, 3.15,
		3.38, 3.68, 16.68, 14.51, 14.52, 12.84, 15.47, 11.86, 2.96, 3.87, 3.31,
		3.16, 3.50, 3.17, 13.18, 14.85, 15.37, 12.73, 12.01, 13.96, 3.69, 3.44,
		3.10, 4.05, 3.94, 3.35, 15.31, 10.97, 15.22, 13.61, 12.35, 12.08, 2.55,
		3.93, 2.92, 3.65, 3.24, 4.02,
	}},
	{"Male", 40, "men between 21 and 40 years of age", [71]float64{
		0, 66.97, 78.90, 86.51, 84.22, 85.50, 16.48, 15.21, 12.65, 13.10, 14.27,
		11.44, 11.75, 10.37, 12.11, 12.18, 9.13, 3.76, 4.30, 4.12, 3.81, 3.52,
		3.48, 13.31, 11.34, 14.58, 12.07, 13.34, 14.30, 3.80, 3.99, 3.58, 3.23,
		3.43, 3.53, 15.94, 14.94, 14.60, 13.14, 16.11, 11.66, 3.18, 3.63, 3.19,
		3.39, 3.25, 3.72, 12.81, 15.93, 15.37, 14.58, 11.43, 13.77, 3.69, 3.18,
		2.92, 3.70, 3.57, 3.29, 15.80, 12.05, 15.68, 15.36, 13.27, 13.31, 2.44,
		4.26, 2.76, 3.39, 3.31, 4.03,
	}},
	{"Male", 60, "men between 41 and 60 years of age", [71]float64{
		0, 64.11, 77.06, 83.04, 88.33, 91.27, 16.04, 14.31, 13.05, 11.76, 13.35,
		10.79, 11.60, 9.78, 11.85, 11.24, 8.81, 3.56, 4.16, 3.94, 3.62, 3.55,
		3.35, 13.22, 10.45, 14.95, 12.27, 11.82, 14.32, 3.71, 3.68, 3.44, 3.30,
		3.23, 3.29, 14.65, 14.66, 14.76, 12.69, 15.40, 11.04, 3.35, 3.59, 3.02,
		3.44, 3.43, 3.93, 13.42, 16.94, 15.65, 15.66, 11.96, 14.21, 3.49, 2.83,
		2.88, 3.33, 3.34, 3.17, 16.19, 13.33, 16.56, 16.51, 14.05, 14.60, 2.25,
		4.32, 2.50, 2.93, 3.13, 3.78,
	}},
	{"Male", maxInt, "men over 60 years of age", [71]float64{
		0, 58.42, 79.73, 79.78, 90.20, 95.31, 15.48, 13.63, 12.21, 11.73, 11.99,
		9.81, 11.46, 8.18, 11.08, 9.91, 8.24, 3.54, 4.31, 3.59, 3.82, 3.36,
		3.28, 14.55, 11.19, 15.29, 12.81, 11.03, 15.02, 3.47, 3.58, 3.10, 3.25,
		2.88, 3.16, 14.06, 14.22, 14.34, 12.42, 14.61, 10.11, 3.13, 3.64, 2.90,
		3.20, 3.89, 4.02, 13.96, 17.74, 15.76, 16.18, 11.87, 14.00, 3.13, 2.39,
		2.74, 3.41, 3.50, 3.11, 16.32, 14.41, 17.54, 16.65, 14.98, 15.18, 2.31,
		4.49, 2.30, 2.68, 2.76, 3.61,
	}},
	{"Female", 20, "females less than 21 years of age", [71]float64{
		0, 73.41, 84.26, 89.01, 89.14, 81.27, 15.61, 14.98, 11.84, 13.21, 14.38,
		13.31, 13.09, 11.05, 12.11, 12.48, 11.30, 3.62, 4.18, 4.20, 3.82, 3.30,
		3.47, 14.47, 13.12, 14.03, 12.67, 14.69, 15.34, 3.60, 4.13, 3.68, 3.09,
		3.48, 3.42, 16.86, 15.93, 16.02, 12.95, 15.06, 12.17, 2.89, 3.44, 2.95,
		3.24, 3.51, 3.02, 13.46, 16.11, 16.66, 13.73, 13.23, 15.70, 3.72, 2.94,
		2.69, 4.14, 3.79, 2.84, 15.30, 11.11, 15.62, 14.69, 12.73, 11.82, 2.54,
		4.17, 2.76, 3.37, 3.19, 4.01,
	}},
	{"Female", 40, "women between 21 and 40 years of age", [71]float64{
		0, 72.14, 80.78, 88.25, 91.91, 87.57, 16.16, 14.64, 12.15, 11.39, 13.87,
		13.08, 12.72, 10.79, 12.20, 12.71, 10.69, 3.68, 4.13, 4.07, 3.79, 3.58,
		3.64, 14.05, 11.92, 14.25, 12.77, 12.84, 14.96, 3.66, 4.05, 3.61, 3.24,
		3.53, 3.31, 15.64, 15.97, 16.41, 12.84, 15.28, 12.06, 3.34, 3.30, 2.69,
		3.44, 3.47, 3.46, 13.15, 17.34, 16.81, 15.57, 12.98, 15.52, 3.71, 2.61,
		2.53, 3.50, 3.57, 2.87, 16.02, 12.67, 16.36, 16.11, 13.56, 12.91, 2.34,
		4.51, 2.54, 3.05, 3.23, 4.18,
	}},
	{"Female", 60, "women between 41 and 60 years of age", [71]float64{
		0, 67.38, 78.62, 86.15, 95.73, 93.45, 16.10, 14.19, 12.62, 9.84, 12.94,
		12.05, 11.19, 10.07, 12.07, 11.98, 10.07, 3.72, 4.03, 3.97, 3.73, 3.69,
		3.56, 14.10, 10.84, 14.51, 13.03, 11.08, 15.00, 3.72, 3.86, 3.50, 3.46,
		3.42, 3.26, 14.43, 16.00, 16.37, 12.58, 14.87, 11.85, 3.49, 3.20, 2.58,
		3.45, 3.65, 3.74, 13.79, 18.16, 17.04, 17.02, 13.41, 15.82, 3.52, 2.21,
		2.40, 2.88, 3.30, 2.71, 16.50, 13.68, 17.29, 17.16, 14.35, 14.41, 2.16,
		4.51, 2.27, 2.73, 3.13, 3.86,
	}},
	{"Female", maxInt, "women over 60 years of age", [71]float64{
		0, 63.48, 78.22, 81.56, 97.17, 96.44, 14.92, 12.73, 12.66, 9.52, 12.43,
		11.39, 10.52, 9.10, 12.00, 10.21, 9.87, 3.61, 3.82, 3.68, 3.61, 3.58,
		3.44, 14.85, 10.93, 14.19, 12.76, 10.08, 15.65, 3.43, 3.70, 3.64, 3.26,
		3.20, 3.04, 13.15, 15.95, 15.73, 11.80, 14.21, 10.81, 3.71, 3.12, 2.74,
		3.26, 3.47, 3.89, 14.19, 18.64, 17.13, 17.98, 13.58, 15.83, 3.39, 1.90,
		2.18, 2.56, 3.38, 2.85, 16.50, 15.15, 18.34, 17.19, 14.70, 15.11, 2.24,
		4.07, 1.81, 2.49, 3.15, 3.66,
	}},
}

// Result holds everything the results page and the API need.
type Result struct {
	Sex, Nick, Country, Category string
	Age                          int
	Q                            [items]int

	SN, SE, SO, SA, SC      float64 // standardized domain scores
	SNP, SEP, SOP, SAP, SCP int     // domain percentiles

	SNFP, SEFP, SOFP, SAFP, SCFP [7]int // facet percentiles, 1..6

	Flev [31]string // "low"/"average"/"high" per facet, 1..30
}

func percentile(s float64) int {
	if s < 32 {
		return 1
	}
	if s > 73 {
		return 99
	}
	return int(const1 - (const2 * s) + (const3 * math.Pow(s, 2)) - (const4 * math.Pow(s, 3)))
}

func level(s float64) string {
	if s < lo {
		return "low"
	}
	if s > hi {
		return "high"
	}
	return "average"
}

// Evaluate scores the given responses. It needs sex "Male" or "Female".
func Evaluate(sex string, age int, nick, country string, q [items]int) (*Result, error) {
	var nt *normTable
	for i := range norms {
		if norms[i].sex == sex && age <= norms[i].maxAge {
			nt = &norms[i]
			break
		}
	}
	if nt == nil {
		return nil, fmt.Errorf("no norms for sex %q", sex)
	}
	norm := nt.norm

	r := &Result{Sex: sex, Age: age, Nick: nick, Country: country, Category: nt.category, Q: q}

	// Score facet scales
	var ss [31]int
	for i := 1; i <= 30; i++ {
		for k := 0; k < 4; k++ {
			ss[i] += q[i+30*k]
		}
	}

	// Number each facet set from 1-6
	var NF, EF, OF, AF, CF [7]int
	for i, j := 1, 0; i <= 6; i, j = i+1, j+4 {
		NF[i] = ss[i+j]
		EF[i] = ss[i+j+1]
		OF[i] = ss[i+j+2]
		AF[i] = ss[i+j+3]
		CF[i] = ss[i+j+4]
	}

	// Score domain scales
	var N, E, O, A, C int
	for i := 1; i <= 6; i++ {
		N += NF[i]
		E += EF[i]
		O += OF[i]
		A += AF[i]
		C += CF[i]
	}

	// Standardize scores
	r.SN = (10 * (float64(N) - norm[1]) / norm[6]) + 50
	r.SE = (10 * (float64(E) - norm[2]) / norm[7]) + 50
	r.SO = (10 * (float64(O) - norm[3]) / norm[8]) + 50
	r.SA = (10 * (float64(A) - norm[4]) / norm[9]) + 50
	r.SC = (10 * (float64(C) - norm[5]) / norm[10]) + 50

	r.SNP = percentile(r.SN)
	r.SEP = percentile(r.SE)
	r.SOP = percentile(r.SO)
	r.SAP = percentile(r.SA)
	r.SCP = percentile(r.SC)

	for i := 1; i <= 6; i++ {
		SNF := 50 + (10 * (float64(NF[i]) - norm[i+10]) / norm[i+16])
		SEF := 50 + (10 * (float64(EF[i]) - norm[i+22]) / norm[i+28])
		SOF := 50 + (10 * (float64(OF[i]) - norm[i+34]) / norm[i+40])
		SAF := 50 + (10 * (float64(AF[i]) - norm[i+46]) / norm[i+52])
		SCF := 50 + (10 * (float64(CF[i]) - norm[i+58]) / norm[i+64])

		r.SNFP[i], r.Flev[i] = percentile(SNF), level(SNF)
		r.SEFP[i], r.Flev[i+6] = percentile(SEF), level(SEF)
		r.SOFP[i], r.Flev[i+12] = percentile(SOF), level(SOF)
		r.SAFP[i], r.Flev[i+18] = percentile(SAF), level(SAF)
		r.SCFP[i], r.Flev[i+24] = percentile(SCF), level(SCF)
	}

	return r, nil
}

var apiLabels = []struct {
	names  [7]string
	domain func(*Result) int
	facets func(*Result) [7]int
}{
	{[7]string{"EXTRAVERSION", "Friendliness", "Gregariousness", "Assertiveness", "Activity Level", "Excitement-Seeking", "Cheerfulness"},
		func(r *Result) int { return r.SEP }, func(r *Result) [7]int { return r.SEFP }},
	{[7]string{"AGREEABLENESS", "Trust", "Morality", "Altruism", "Cooperation", "Modesty", "Sympathy"},
		func(r *Result) int { return r.SAP }, func(r *Result) [7]int { return r.SAFP }},
	{[7]string{"CONSCIENTIOUSNESS", "Self-Efficacy", "Orderliness", "Dutifulness", "Achievement-Striving", "Self-Discipline", "Cautiousness"},
		func(r *Result) int { return r.SCP }, func(r *Result) [7]int { return r.SCFP }},
	{[7]string{"NEUROTICISM", "Anxiety", "Anger", "Depression", "Self-Consciousness", "Immoderation", "Vulnerability"},
		func(r *Result) int { return r.SNP }, func(r *Result) [7]int { return r.SNFP }},
	{[7]string{"OPENNESS", "Imagination", "Artistic Interests", "Emotionality", "Adventurousness", "Intellect", "Liberalism"},
		func(r *Result) int { return r.SOP }, func(r *Result) [7]int { return r.SOFP }},
}

// JSON renders the /results_api response with the same key order and
// formatting as Python's json.dumps() in the original evaluator.
func (r *Result) JSON() []byte {
	var b bytes.Buffer
	b.WriteString("{")
	for gi, g := range apiLabels {
		facets := g.facets(r)
		for i, name := range g.names {
			if gi > 0 || i > 0 {
				b.WriteString(", ")
			}
			v := facets[i]
			if i == 0 {
				v = g.domain(r)
			}
			fmt.Fprintf(&b, "%q: %d", name, v)
		}
	}
	b.WriteString("}")
	return b.Bytes()
}
