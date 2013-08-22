#!/usr/bin/env perl

use CGI qw(:cgi-lib);
# require("cgi-lib.pl");

MAIN:
{
  # Read in identifying information
  &ReadParse(*input);

  # Print the header
  print &PrintHeader;
  print &HtmlTop ("IPIP-NEO-PI Items 181-240");

  # Extract identifying variables
  ($Sex = $input{'Sex'});
  ($Age = $input{'Age'});
  ($Nick = $input{'Nick'});
  ($Country = $input{'Country'});
  # Get the item responses
  ($Q[1] = $input{'Q1'});
  ($Q[2] = $input{'Q2'});
  ($Q[3] = $input{'Q3'});
  ($Q[4] = $input{'Q4'});
  ($Q[5] = $input{'Q5'});
  ($Q[6] = $input{'Q6'});
  ($Q[7] = $input{'Q7'});
  ($Q[8] = $input{'Q8'});
  ($Q[9] = $input{'Q9'});
  ($Q[10] = $input{'Q10'});
  ($Q[11] = $input{'Q11'});
  ($Q[12] = $input{'Q12'});
  ($Q[13] = $input{'Q13'});
  ($Q[14] = $input{'Q14'});
  ($Q[15] = $input{'Q15'});
  ($Q[16] = $input{'Q16'});
  ($Q[17] = $input{'Q17'});
  ($Q[18] = $input{'Q18'});
  ($Q[19] = $input{'Q19'});
  ($Q[20] = $input{'Q20'});
  ($Q[21] = $input{'Q21'});
  ($Q[22] = $input{'Q22'});
  ($Q[23] = $input{'Q23'});
  ($Q[24] = $input{'Q24'});
  ($Q[25] = $input{'Q25'});
  ($Q[26] = $input{'Q26'});
  ($Q[27] = $input{'Q27'});
  ($Q[28] = $input{'Q28'});
  ($Q[29] = $input{'Q29'});
  ($Q[30] = $input{'Q30'});
  ($Q[31] = $input{'Q31'});
  ($Q[32] = $input{'Q32'});
  ($Q[33] = $input{'Q33'});
  ($Q[34] = $input{'Q34'});
  ($Q[35] = $input{'Q35'});
  ($Q[36] = $input{'Q36'});
  ($Q[37] = $input{'Q37'});
  ($Q[38] = $input{'Q38'});
  ($Q[39] = $input{'Q39'});
  ($Q[40] = $input{'Q40'});
  ($Q[41] = $input{'Q41'});
  ($Q[42] = $input{'Q42'});
  ($Q[43] = $input{'Q43'});
  ($Q[44] = $input{'Q44'});
  ($Q[45] = $input{'Q45'});
  ($Q[46] = $input{'Q46'});
  ($Q[47] = $input{'Q47'});
  ($Q[48] = $input{'Q48'});
  ($Q[49] = $input{'Q49'});
  ($Q[50] = $input{'Q50'});
  ($Q[51] = $input{'Q51'});
  ($Q[52] = $input{'Q52'});
  ($Q[53] = $input{'Q53'});
  ($Q[54] = $input{'Q54'});
  ($Q[55] = $input{'Q55'});
  ($Q[56] = $input{'Q56'});
  ($Q[57] = $input{'Q57'});
  ($Q[58] = $input{'Q58'});
  ($Q[59] = $input{'Q59'});
  ($Q[60] = $input{'Q60'});
  ($Q[61] = $input{'Q61'});
  ($Q[62] = $input{'Q62'});
  ($Q[63] = $input{'Q63'});
  ($Q[64] = $input{'Q64'});
  ($Q[65] = $input{'Q65'});
  ($Q[66] = $input{'Q66'});
  ($Q[67] = $input{'Q67'});
  ($Q[68] = $input{'Q68'});
  ($Q[69] = $input{'Q69'});
  ($Q[70] = $input{'Q70'});
  ($Q[71] = $input{'Q71'});
  ($Q[72] = $input{'Q72'});
  ($Q[73] = $input{'Q73'});
  ($Q[74] = $input{'Q74'});
  ($Q[75] = $input{'Q75'});
  ($Q[76] = $input{'Q76'});
  ($Q[77] = $input{'Q77'});
  ($Q[78] = $input{'Q78'});
  ($Q[79] = $input{'Q79'});
  ($Q[80] = $input{'Q80'});
  ($Q[81] = $input{'Q81'});
  ($Q[82] = $input{'Q82'});
  ($Q[83] = $input{'Q83'});
  ($Q[84] = $input{'Q84'});
  ($Q[85] = $input{'Q85'});
  ($Q[86] = $input{'Q86'});
  ($Q[87] = $input{'Q87'});
  ($Q[88] = $input{'Q88'});
  ($Q[89] = $input{'Q89'});
  ($Q[90] = $input{'Q90'});
  ($Q[91] = $input{'Q91'});
  ($Q[92] = $input{'Q92'});
  ($Q[93] = $input{'Q93'});
  ($Q[94] = $input{'Q94'});
  ($Q[95] = $input{'Q95'});
  ($Q[96] = $input{'Q96'});
  ($Q[97] = $input{'Q97'});
  ($Q[98] = $input{'Q98'});
  ($Q[99] = $input{'Q99'});
  ($Q[100] = $input{'Q100'});
  ($Q[101] = $input{'Q101'});
  ($Q[102] = $input{'Q102'});
  ($Q[103] = $input{'Q103'});
  ($Q[104] = $input{'Q104'});
  ($Q[105] = $input{'Q105'});
  ($Q[106] = $input{'Q106'});
  ($Q[107] = $input{'Q107'});
  ($Q[108] = $input{'Q108'});
  ($Q[109] = $input{'Q109'});
  ($Q[110] = $input{'Q110'});
  ($Q[111] = $input{'Q111'});
  ($Q[112] = $input{'Q112'});
  ($Q[113] = $input{'Q113'});
  ($Q[114] = $input{'Q114'});
  ($Q[115] = $input{'Q115'});
  ($Q[116] = $input{'Q116'});
  ($Q[117] = $input{'Q117'});
  ($Q[118] = $input{'Q118'});
  ($Q[119] = $input{'Q119'});
  ($Q[120] = $input{'Q120'});
  ($Q[121] = $input{'Q121'});
  ($Q[122] = $input{'Q122'});
  ($Q[123] = $input{'Q123'});
  ($Q[124] = $input{'Q124'});
  ($Q[125] = $input{'Q125'});
  ($Q[126] = $input{'Q126'});
  ($Q[127] = $input{'Q127'});
  ($Q[128] = $input{'Q128'});
  ($Q[129] = $input{'Q129'});
  ($Q[130] = $input{'Q130'});
  ($Q[131] = $input{'Q131'});
  ($Q[132] = $input{'Q132'});
  ($Q[133] = $input{'Q133'});
  ($Q[134] = $input{'Q134'});
  ($Q[135] = $input{'Q135'});
  ($Q[136] = $input{'Q136'});
  ($Q[137] = $input{'Q137'});
  ($Q[138] = $input{'Q138'});
  ($Q[139] = $input{'Q139'});
  ($Q[140] = $input{'Q140'});
  ($Q[141] = $input{'Q141'});
  ($Q[142] = $input{'Q142'});
  ($Q[143] = $input{'Q143'});
  ($Q[144] = $input{'Q144'});
  ($Q[145] = $input{'Q145'});
  ($Q[146] = $input{'Q146'});
  ($Q[147] = $input{'Q147'});
  ($Q[148] = $input{'Q148'});
  ($Q[149] = $input{'Q149'});
  ($Q[150] = $input{'Q150'});
  ($Q[151] = $input{'Q151'});
  ($Q[152] = $input{'Q152'});
  ($Q[153] = $input{'Q153'});
  ($Q[154] = $input{'Q154'});
  ($Q[155] = $input{'Q155'});
  ($Q[156] = $input{'Q156'});
  ($Q[157] = $input{'Q157'});
  ($Q[158] = $input{'Q158'});
  ($Q[159] = $input{'Q159'});
  ($Q[160] = $input{'Q160'});
  ($Q[161] = $input{'Q161'});
  ($Q[162] = $input{'Q162'});
  ($Q[163] = $input{'Q163'});
  ($Q[164] = $input{'Q164'});
  ($Q[165] = $input{'Q165'});
  ($Q[166] = $input{'Q166'});
  ($Q[167] = $input{'Q167'});
  ($Q[168] = $input{'Q168'});
  ($Q[169] = $input{'Q169'});
  ($Q[170] = $input{'Q170'});
  ($Q[171] = $input{'Q171'});
  ($Q[172] = $input{'Q172'});
  ($Q[173] = $input{'Q173'});
  ($Q[174] = $input{'Q174'});
  ($Q[175] = $input{'Q175'});
  ($Q[176] = $input{'Q176'});
  ($Q[177] = $input{'Q177'});
  ($Q[178] = $input{'Q178'});
  ($Q[179] = $input{'Q179'});
  ($Q[180] = $input{'Q180'});

#HTML for items 181-240
  print <<ENDOFTEXT;

<form method=post action="ipipneo5.cgi">
ENDOFTEXT

  print "<input type=\"hidden\" name=\"Nick\" value=\"$Nick\">\n";
  print "<input type=\"hidden\" name=\"Sex\" value=\"$Sex\">\n";
  print "<input type=\"hidden\" name=\"Age\" value=\"$Age\">\n";
  print "<input type=\"hidden\" name=\"Country\" value=\"$Country\">\n";
  for ($i = 1; $i < 181; $i++) {
  print "<input type=\"hidden\" name=\"Q$i\" value=\"$Q[$i]\">\n";
}
  print <<ENDOFTEXT;
<table border>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
181. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Am relaxed most of the time.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q181" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q181" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q181" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q181" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q181" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
182. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Often feel uncomfortable around others.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q182" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q182" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q182" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q182" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q182" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
183. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Seldom daydream.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q183" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q183" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q183" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q183" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q183" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
184. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Distrust people.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q184" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q184" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q184" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q184" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q184" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
185. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Misjudge situations.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q185" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q185" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q185" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q185" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q185" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
186. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Seldom get mad.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q186" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q186" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q186" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q186" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q186" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
187. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Want to be left alone.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q187" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q187" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q187" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q187" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q187" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
188. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Do not like poetry.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q188" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q188" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q188" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q188" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q188" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
189. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Put people under pressure.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q189" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q189" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q189" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q189" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q189" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
190. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Leave a mess in my room.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q190" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q190" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q190" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q190" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q190" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
191. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Feel that my life lacks direction.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q191" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q191" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q191" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q191" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q191" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
192. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Keep in the background.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q192" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q192" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q192" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q192" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q192" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
193. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Am not easily affected by my emotions.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q193" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q193" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q193" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q193" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q193" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
194. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Am indifferent to the feelings of others.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q194" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q194" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q194" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q194" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q194" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
195. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Break my promises.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q195" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q195" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q195" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q195" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q195" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
196. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Am not embarrassed easily.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q196" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q196" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q196" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q196" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q196" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
197. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Like to take my time.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q197" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q197" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q197" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q197" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q197" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
198. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Don't like the idea of change.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q198" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q198" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q198" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q198" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q198" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
199. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Yell at people.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q199" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q199" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q199" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q199" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q199" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
200. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Demand quality.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q200" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q200" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q200" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q200" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q200" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
201. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Easily resist temptations.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q201" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q201" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q201" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q201" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q201" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
202. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Willing to try anything once.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q202" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q202" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q202" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q202" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q202" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
203. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Avoid philosophical discussions.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q203" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q203" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q203" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q203" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q203" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
204. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Have a high opinion of myself.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q204" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q204" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q204" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q204" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q204" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
205. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Waste my time.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q205" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q205" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q205" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q205" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q205" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
206. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Can handle complex problems.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q206" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q206" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q206" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q206" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q206" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
207. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Laugh aloud.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q207" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q207" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q207" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q207" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q207" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
208. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Believe laws should be strictly enforced.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q208" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q208" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q208" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q208" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q208" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
209. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Believe in an eye for an eye.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q209" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q209" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q209" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q209" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q209" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
210. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Rush into things.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q210" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q210" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q210" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q210" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q210" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
211. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Am not easily disturbed by events.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q211" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q211" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q211" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q211" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q211" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
212. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Avoid contacts with others.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q212" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q212" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q212" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q212" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q212" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
213. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Do not have a good imagination.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q213" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q213" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q213" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q213" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q213" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
214. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Suspect hidden motives in others.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q214" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q214" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q214" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q214" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q214" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
215. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Don't understand things.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q215" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q215" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q215" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q215" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q215" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
216. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Am not easily annoyed.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q216" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q216" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q216" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q216" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q216" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
217. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Don't like crowded events.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q217" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q217" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q217" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q217" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q217" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
218. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Do not enjoy going to art museums.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q218" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q218" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q218" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q218" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q218" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
219. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Pretend to be concerned for others.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q219" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q219" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q219" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q219" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q219" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
220. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Leave my belongings around.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q220" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q220" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q220" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q220" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q220" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
221. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Seldom feel blue.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q221" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q221" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q221" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q221" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q221" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
222. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Have little to say.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q222" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q222" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q222" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q222" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q222" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
223. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Rarely notice my emotional reactions.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q223" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q223" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q223" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q223" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q223" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
224. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Make people feel uncomfortable.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q224" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q224" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q224" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q224" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q224" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
225. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Get others to do my duties.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q225" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q225" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q225" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q225" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q225" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
226. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Am comfortable in unfamiliar situations.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q226" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q226" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q226" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q226" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q226" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
227. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Like a leisurely lifestyle.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q227" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q227" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q227" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q227" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q227" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
228. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Am a creature of habit.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q228" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q228" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q228" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q228" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q228" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
229. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Insult people.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q229" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q229" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q229" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q229" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q229" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
230. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Am not highly motivated to succeed.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q230" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q230" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q230" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q230" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q230" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
231. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Am able to control my cravings.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q231" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q231" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q231" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q231" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q231" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
232. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Seek danger.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q232" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q232" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q232" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q232" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q232" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
233. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Have difficulty understanding abstract ideas.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q233" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q233" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q233" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q233" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q233" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
234. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Know the answers to many questions.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q234" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q234" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q234" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q234" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q234" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
235. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Need a push to get started.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q235" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q235" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q235" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q235" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q235" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
236. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Know how to cope.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q236" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q236" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q236" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q236" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q236" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
237. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Amuse my friends.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q237" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q237" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q237" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q237" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q237" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
238. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Believe that we coddle criminals too much.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q238" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q238" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q238" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q238" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q238" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
239. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Try not to think about the needy.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q239" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q239" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q239" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q239" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q239" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
240. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Do crazy things.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q240" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q240" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q240" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q240" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q240" VALUE="1"></CENTER></TD>
</TR>

</table>

<p><br><input type="submit" value="Send "><b>&nbsp;&nbsp;This
will send your answers to be scored and take you to the next 60 questions.</b>
</form>
</body>
</html>
ENDOFTEXT
}
