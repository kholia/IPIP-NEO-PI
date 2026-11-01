#!/usr/bin/env python3
"""
Builds ipipneo/views/index.html and shortipipneo.html from saved copies of
the official pages, so they can be refreshed when Dr. Johnson updates them.

    python3 upstream_views.py <saved pages dir> ipipneo/views

The saved pages dir must hold UTF-8 copies (the originals are Windows-1252,
despite declaring ISO-8859-1) of:
    intro.html  ipipneo120.htm
    p1.html     shortipipneo1.cgi (items 1-60)
    p2.html     shortipipneo2.cgi (items 61-120)

Save them from a browser; do not script it: never submit the final page
(shortipipneo3.cgi) of the live site, which feeds Dr. Johnson's research
database.

Deliberate changes to the official pages (each asserted to apply exactly
once, so the script fails loudly when upstream changes):
  * all 120 items on one page; form posts to our own URLs
  * the red notice explains this version's (2021) norms instead of the
    online version's new combined norms
  * client-side validation covers 120 items and the gender question, and
    focuses the first unanswered item correctly
  * a missing ">" on the "Other" gender radio button is fixed
"""
import re, sys
up, out = sys.argv[1], sys.argv[2]

def read(name):
    return open('%s/%s' % (up, name), encoding='utf-8').read()

def sub1(s, old, new):
    assert s.count(old) == 1, (s.count(old), old[:60])
    return s.replace(old, new)

def write(name, title, body):
    assert '{{' not in body and '}}' not in body
    with open('%s/%s' % (out, name), 'w') as f:
        f.write('{{define "title"}}%s{{end}}\n{{define "content"}}\n%s\n{{end}}\n' % (title, body.strip('\n')))

# --- Intro page (ipipneo120.htm) ---
intro = read('intro.html')
body = re.search(r'<body[^>]*>(.*)</body>', intro, re.S).group(1)
body = sub1(body, 'action="shortipipneo1.cgi"', 'action="shortipipneo"')
body = sub1(body, 'will take you to the first 60 questions only if', 'will take you to the questions only if')
write('index.html', 'Short Form for the IPIP NEO-PI, Introductory Information', body)

# --- Items page: page 1 (items 1-60) + page 2 (items 61-120) on one page ---
p1, p2 = read('p1.html'), read('p2.html')
script = re.search(r'<script type="text/javascript">//<!\[CDATA\[(.*?)//\]\]></script>', p1, re.S).group(1)
script = script.replace('i <= 60', 'i <= 120').replace('check all 60 radio', 'check all 120 radio')
script = sub1(script, '''	document.getElementById("sexError").style.display = "none";
''', '''	document.getElementById("sexError").style.display = "none";
	document.getElementById("genderError").style.display = "none";
''')
script = sub1(script, '''	if (isNaN(formObject.Age.value)''', '''	if (!isChecked(formObject.Gender))
    {
		document.getElementById("genderError").style.display = "inline";
        formObject.Gender[0].focus();
        err=true;
    }

	if (isNaN(formObject.Age.value)''')
# Upstream focuses elements[foc*5], which is off since the gender fields were added.
script = sub1(script, '''			foc=foc*5;
			formObject.elements[foc].focus();''', '''			formObject.elements["Q"+foc][0].focus();''')

main = p1[p1.index('<div id="main">'):p1.index('<p><input TYPE="submit"')]
main = sub1(main, '''After you have answered
the first 60 of the 120 total items, press the send button. at the bottom
of this page. This will send your responses to the scoring program and
take you to a page with the next 60 questions. After you complete this second page of 60 questions, pressing the send button will return an interpretive
report to you.''', '''After you have answered
all 120 items, press the send button at the bottom of this page. This will
send your responses to the scoring program and return an interpretive
report to you.''')
main = sub1(main, 'action="shortipipneo2.cgi"', 'action="results"')
red = re.search(r'<p style="color:red; font-size:20px">.*?</p>', main, re.S).group(0)
main = sub1(main, red, '''<p style="color:red; font-size:20px">This offline version of the inventory compares your scores to those of
people of your sex assigned at birth (male or female) and roughly your age, using the norms of the 2021 version of the
online inventory. (The online inventory is being revised to compare respondents&apos; scores to <strong>a sample of over
two million people without regard to sex, gender, age, or nationality</strong>.) Reports cannot yet be produced for
respondents who select Intersex, but their responses are still saved. Your current gender identity, age, and nationality
are recorded to help build comparison groups for future versions of this inventory.</p>''')
# Upstream is missing the ">" of this radio button.
main = sub1(main, 'value="9" \n<label', 'value="9">\n<label')

table2 = p2[p2.index('<table border>'):p2.rindex('</form>')]
body = ('<script type="text/javascript">' + script + '</script>\n' + main
        + '<br>&nbsp;\n' + table2 + '</form>\n</div>\n')
write('shortipipneo.html', 'IPIP-NEO-PI Short Form Items', body)
