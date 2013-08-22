#!/usr/bin/env perl

use CGI qw(:cgi-lib);
# require("cgi-lib.pl");

MAIN:
{
# Print the header
  print &PrintHeader;
  print &HtmlTop ("IPIP-NEO-PI Items 241-300");

  # Read in identifying information
  &ReadParse(*input);

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
  ($Q[181] = $input{'Q181'});
  ($Q[182] = $input{'Q182'});
  ($Q[183] = $input{'Q183'});
  ($Q[184] = $input{'Q184'});
  ($Q[185] = $input{'Q185'});
  ($Q[186] = $input{'Q186'});
  ($Q[187] = $input{'Q187'});
  ($Q[188] = $input{'Q188'});
  ($Q[189] = $input{'Q189'});
  ($Q[190] = $input{'Q190'});
  ($Q[191] = $input{'Q191'});
  ($Q[192] = $input{'Q192'});
  ($Q[193] = $input{'Q193'});
  ($Q[194] = $input{'Q194'});
  ($Q[195] = $input{'Q195'});
  ($Q[196] = $input{'Q196'});
  ($Q[197] = $input{'Q197'});
  ($Q[198] = $input{'Q198'});
  ($Q[199] = $input{'Q199'});
  ($Q[200] = $input{'Q200'});
  ($Q[201] = $input{'Q201'});
  ($Q[202] = $input{'Q202'});
  ($Q[203] = $input{'Q203'});
  ($Q[204] = $input{'Q204'});
  ($Q[205] = $input{'Q205'});
  ($Q[206] = $input{'Q206'});
  ($Q[207] = $input{'Q207'});
  ($Q[208] = $input{'Q208'});
  ($Q[209] = $input{'Q209'});
  ($Q[210] = $input{'Q210'});
  ($Q[211] = $input{'Q211'});
  ($Q[212] = $input{'Q212'});
  ($Q[213] = $input{'Q213'});
  ($Q[214] = $input{'Q214'});
  ($Q[215] = $input{'Q215'});
  ($Q[216] = $input{'Q216'});
  ($Q[217] = $input{'Q217'});
  ($Q[218] = $input{'Q218'});
  ($Q[219] = $input{'Q219'});
  ($Q[220] = $input{'Q220'});
  ($Q[221] = $input{'Q221'});
  ($Q[222] = $input{'Q222'});
  ($Q[223] = $input{'Q223'});
  ($Q[224] = $input{'Q224'});
  ($Q[225] = $input{'Q225'});
  ($Q[226] = $input{'Q226'});
  ($Q[227] = $input{'Q227'});
  ($Q[228] = $input{'Q228'});
  ($Q[229] = $input{'Q229'});
  ($Q[230] = $input{'Q230'});
  ($Q[231] = $input{'Q231'});
  ($Q[232] = $input{'Q232'});
  ($Q[233] = $input{'Q233'});
  ($Q[234] = $input{'Q234'});
  ($Q[235] = $input{'Q235'});
  ($Q[236] = $input{'Q236'});
  ($Q[237] = $input{'Q237'});
  ($Q[238] = $input{'Q238'});
  ($Q[239] = $input{'Q239'});
  ($Q[240] = $input{'Q240'});

#HTML for items 241-300

  print <<ENDOFTEXT;

<form method=post action="ipipneo6.cgi">
ENDOFTEXT

  print "<input type=\"hidden\" name=\"Nick\" value=\"$Nick\">\n";
  print "<input type=\"hidden\" name=\"Sex\" value=\"$Sex\">\n";
  print "<input type=\"hidden\" name=\"Age\" value=\"$Age\">\n";
  print "<input type=\"hidden\" name=\"Country\" value=\"$Country\">\n";
   for ($i = 1; $i < 241; $i++) {
  print "<input type=\"hidden\" name=\"Q$i\" value=\"$Q[$i]\">\n";
}
  print <<ENDOFTEXT;
<table border>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
241. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Don't worry about things that have already happened.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q241" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q241" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q241" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q241" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q241" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
242. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Am not really interested in others.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q242" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q242" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q242" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q242" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q242" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
243. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Seldom get lost in thought.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q243" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q243" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q243" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q243" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q243" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
244. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Am wary of others.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q244" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q244" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q244" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q244" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q244" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
245. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Have little to contribute.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q245" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q245" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q245" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q245" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q245" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
246. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Keep my cool.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q246" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q246" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q246" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q246" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q246" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
247. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Avoid crowds.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q247" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q247" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q247" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q247" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q247" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
248. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Do not like concerts.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q248" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q248" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q248" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q248" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q248" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
249. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Take advantage of others.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q249" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q249" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q249" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q249" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q249" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
250. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Am not bothered by messy people.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q250" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q250" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q250" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q250" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q250" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
251. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Feel comfortable with myself.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q251" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q251" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR> <INPUT TYPE="RADIO" NAME="Q251" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q251" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q251" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
252. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Don't like to draw attention to myself.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q252" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q252" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q252" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q252" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q252" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
253. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Experience very few emotional highs and lows.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q253" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q253" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q253" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q253" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q253" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
254. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Turn my back on others.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q254" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q254" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q254" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q254" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q254" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
255. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Do the opposite of what is asked.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q255" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q255" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q255" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q255" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q255" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
256. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Am not bothered by difficult social situations.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q256" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q256" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q256" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q256" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q256" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
257. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Let things proceed at their own pace.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q257" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q257" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q257" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q257" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q257" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
258. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Dislike new foods.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q258" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q258" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q258" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q258" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q258" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
259. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Get back at others.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q259" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q259" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q259" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q259" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q259" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
260. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Do just enough work to get by.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q260" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q260" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q260" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q260" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q260" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
261. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Never spend more than I can afford.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q261" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q261" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q261" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q261" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q261" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
262. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Would never go hang gliding or bungee jumping.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q262" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q262" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q262" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q262" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q262" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
263. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Am not interested in theoretical discussions.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q263" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q263" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q263" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q263" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q263" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
264. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Boast about my virtues.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q264" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q264" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q264" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q264" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q264" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
265. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Have difficulty starting tasks.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q265" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q265" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q265" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q265" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q265" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
266. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Readily overcome setbacks.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q266" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q266" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q266" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q266" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q266" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
267. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Am not easily amused.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q267" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q267" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q267" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q267" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q267" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
268. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Believe that we should be tough on crime.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q268" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q268" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q268" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q268" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q268" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
269. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Believe people should fend for themselves.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q269" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q269" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q269" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q269" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q269" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
270. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Act without thinking.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q270" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q270" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q270" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q270" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q270" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
271. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Adapt easily to new situations.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q271" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q271" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q271" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q271" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q271" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
272. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Keep others at a distance.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q272" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q272" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q272" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q272" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q272" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
273. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Have difficulty imagining things.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q273" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q273" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q273" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q273" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q273" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
274. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Believe that people are essentially evil.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q274" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q274" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q274" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q274" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q274" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
275. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Don't see the consequences of things.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q275" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q275" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q275" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q275" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q275" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
276. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Rarely complain.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q276" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q276" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q276" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q276" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q276" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
277. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Seek quiet.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q277" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q277" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q277" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q277" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q277" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
278. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Do not enjoy watching dance performances.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q278" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q278" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q278" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q278" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q278" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
279. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Obstruct others' plans.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q279" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q279" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q279" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q279" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q279" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
280. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Am not bothered by disorder.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q280" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q280" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q280" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q280" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q280" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
281. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Am very pleased with myself.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q281" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q281" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q281" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q281" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q281" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
282. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Hold back my opinions.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q282" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q282" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q282" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q282" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q282" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
283. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Don't understand people who get emotional.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q283" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q283" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q283" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q283" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q283" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
284. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Take no time for others.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q284" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q284" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q284" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q284" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q284" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
285. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Misrepresent the facts.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q285" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q285" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q285" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q285" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q285" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
286. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Am able to stand up for myself.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q286" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q286" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q286" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q286" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q286" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
287. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>React slowly.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q287" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q287" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q287" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q287" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q287" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
288. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Am attached to conventional ways.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q288" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q288" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q288" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q288" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q288" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
289. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Hold a grudge.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q289" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q289" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q289" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q289" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q289" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
290. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Put little time and effort into my work.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q290" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q290" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q290" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q290" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q290" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
291. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Never splurge.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q291" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q291" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q291" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q291" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q291" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
292. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Dislike loud music.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q292" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q292" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q292" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q292" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q292" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
293. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Avoid difficult reading material.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q293" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q293" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q293" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q293" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q293" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
294. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Make myself the center of attention.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q294" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q294" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q294" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q294" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q294" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
295. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Postpone decisions.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q295" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q295" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q295" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q295" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q295" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
296. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Am calm even in tense situations.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q296" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q296" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q296" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q296" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q296" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
297. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Seldom joke around.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q297" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q297" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q297" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q297" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q297" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
298. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Like to stand during the national anthem.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q298" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q298" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q298" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q298" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q298" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
299. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Can't stand weak people.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q299" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q299" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q299" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q299" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q299" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
300. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Often make last-minute plans.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q300" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q300" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q300" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q300" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q300" VALUE="1"></CENTER></TD>
</TR>

<tr>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
A. </TD>
<TD WIDTH="28%"><b>I have tried to answer all of these questions honestly
and accurately. </b></td>

<td WIDTH="14%">
<CENTER>Very<BR>
Inaccurate<BR>
<input TYPE="RADIO" NAME="A" VALUE="1"></CENTER></td>

<td WIDTH="13%">
<CENTER>Moderately<BR>
Inaccurate<BR>
<input TYPE="RADIO" NAME="A" VALUE="2"></CENTER></td>

<td WIDTH="17%">
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<input TYPE="RADIO" NAME="A" VALUE="3"></td>

<td WIDTH="12%">
<CENTER>Moderately<BR>
Accurate<BR>
<input TYPE="RADIO" NAME="A" VALUE="4"></CENTER></td>

<td WIDTH="11%">
<CENTER>Very<BR>
Accurate<BR>
<input TYPE="RADIO" NAME="A" VALUE="5"></CENTER></td>
</tr>

<tr>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
B. </TD>
<TD WIDTH="28%"><b>I have responded to all of the statements. </b></td>

<td WIDTH="14%"><b>Yes</b>
<br><input TYPE="RADIO" NAME="B" VALUE="Yes"></td>

<td WIDTH="13%"><b>No</b>
<br><input TYPE="RADIO" NAME="B" VALUE="No"></td>
</tr>

<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
C. </TD>
<TD WIDTH="28%"><b>I have entered my responses in the correct areas.</b>
</td>

<td WIDTH="14%"><b>Yes</b>
<br><input TYPE="RADIO" NAME="C" VALUE="Yes"></td>

<td WIDTH="13%"><b>No</b>
<br><input TYPE="RADIO" NAME="C" VALUE="No"></td>
</tr>
</table>

<p>
<b>PLEASE NOTE:</b> Your results should appear on your screen within moments after clicking the Send button. If nothing happens, something has gone wrong. Clicking the button again and again will not help.</p>
<p>
As I indicated in the warning at the beginning of the test, I am a psychologist, not a computer technician, so I have no definitive way of solving any person's particular computer problem.  For people who were unable to complete the test, sometimes using a better computer, faster internet connection, or just taking the test on a different day and time led to success. If you experience difficulties, you can email me if you like (j5j at psu.edu), but I won't be able to tell you anything more than what I have just said here.</p>
<p><br><input type="submit" value="Send "><b>&nbsp;&nbsp;This
will send your answers to be scored and post your results.</b>
</form>
</body>
</html>
ENDOFTEXT
}
