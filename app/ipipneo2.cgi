#!/usr/bin/env perl

use CGI qw(:cgi-lib);
# require("cgi-lib.pl");

MAIN:
{
# Read in identifying information
  &ReadParse(*input);

# Print the header
  print &PrintHeader;
  print &HtmlTop ("IPIP-NEO-PI Items 61-120");

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


  if ($Sex ne "Male" && $Sex ne "Female") {
    print <<ENDOFTEXT;

You did not indicate your sex at the beginning of the inventory. Your answers
cannot be normed properly unless you indicate whether you are male or female.
Please return to the inventory and indicate your sex.
ENDOFTEXT
  exit;
}

#Generate random nickname if nickname is blank
    if ($Nick !~ /\w/) {
    $Nick = &random_password(23);
}
#Make sure Age is numeric
  if ($Age =~ /\D/) {
    print <<ENDOFTEXT;
You did not enter your age in numeric digits. For example if you have lived for three decades, you must enter 30 rather than thirty in the Age box. Please return to the previous page and enter your age properly.
ENDOFTEXT
  exit;
}

#Make sure respondent is at least 10 years old
  if ($Age < 10) {
    print <<ENDOFTEXT;

You did not indicate how old you are at the beginning of the inventory, or you
typed in an age that is too young. Your answers cannot be normed properly
unless you type in a valid age. Please return to the inventory and change your response.
ENDOFTEXT
  exit;
}
  if ($Age > 99) {
    print <<ENDOFTEXT;

Are you really as old as you have indicated? If you really are that old, congratulations on living so long! But to make data processing easier, I want to limit ages to two-digit numbers. If you really are 100 years old or older, please return to the previous page and enter a 99 for your age.
ENDOFTEXT
  exit;
}

  if ($Country !~ /\w/) {
    print <<ENDOFTEXT;

You did not indicate which country you are from. Indicating where you are from will help build better norms that will improve the validity of this test. Please return to the previous page and indicate the country to which you feel you belong the most.
ENDOFTEXT
  exit;
}

#Truncate long Nicknames
$str_length = length($Nick);
  if ($str_length > 23) {
  ($Nick = substr($Nick, 0, 23));
}

#Pad short Nicknames
  $blank_str = " ";
  while ($str_length < 23) {
  $Nick .= $blank_str;
  $str_length = length($Nick);
}

#HTML for items 61-121
  print <<ENDOFTEXT;
  <HTML><HEAD><TITLE>IPIP-NEO-PI Items 61-120</TITLE></HEAD><Body><p>
ENDOFTEXT

  print <<ENDOFTEXT;

  <form method=post action="ipipneo3.cgi">
ENDOFTEXT

  print "<input type=\"hidden\" name=\"Nick\" value=\"$Nick\">\n";
  print "<input type=\"hidden\" name=\"Sex\" value=\"$Sex\">\n";
  print "<input type=\"hidden\" name=\"Age\" value=\"$Age\">\n";
  print "<input type=\"hidden\" name=\"Country\" value=\"$Country\">\n";
  for ($i = 1; $i < 61; $i++) {
  print "<input type=\"hidden\" name=\"Q$i\" value=\"$Q[$i]\">\n";
}
  print <<ENDOFTEXT;
<table border>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
61. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Am afraid of many things.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q61" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q61" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q61" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q61" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q61" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
62. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Feel comfortable around people.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q62" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q62" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q62" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q62" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q62" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
63. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Love to daydream.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q63" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q63" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q63" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q63" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q63" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
64. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Trust what people say.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q64" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q64" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q64" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q64" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q64" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
65. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Handle tasks smoothly.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q65" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q65" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q65" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q65" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q65" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
66. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Get upset easily.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q66" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q66" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q66" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q66" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q66" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
67. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Enjoy being part of a group.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q67" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q67" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q67" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q67" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q67" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
68. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>See beauty in things that others might not notice.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q68" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q68" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q68" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q68" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q68" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
69. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Use flattery to get ahead.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q69" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q69" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q69" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q69" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q69" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
70. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Want everything to be "just right."</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q70" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q70" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q70" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q70" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q70" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
71. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Am often down in the dumps.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q71" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q71" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q71" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q71" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q71" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
72. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Can talk others into doing things.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q72" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q72" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q72" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q72" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q72" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
73. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Am passionate about causes.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q73" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q73" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q73" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q73" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q73" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
74. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Love to help others.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q74" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q74" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q74" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q74" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q74" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
75. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Pay my bills on time.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q75" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q75" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q75" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q75" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q75" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
76. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Find it difficult to approach others.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q76" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q76" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q76" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q76" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q76" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
77. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Do a lot in my spare time.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q77" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q77" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q77" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q77" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q77" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
78. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Interested in many things.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q78" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q78" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q78" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q78" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q78" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
79. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Hate to seem pushy.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q79" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q79" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q79" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q79" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q79" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
80. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Turn plans into actions.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q80" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q80" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q80" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q80" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q80" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
81. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Do things I later regret.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q81" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q81" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q81" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q81" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q81" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
82. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Love action.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q82" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q82" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q82" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q82" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q82" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
83. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Have a rich vocabulary.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q83" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q83" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q83" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q83" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q83" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
84. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Consider myself an average person.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q84" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q84" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q84" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q84" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q84" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
85. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Start tasks right away.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q85" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q85" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q85" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q85" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q85" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
86. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Feel that I'm unable to deal with things.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q86" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q86" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q86" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q86" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q86" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
87. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Express childlike joy.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q87" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q87" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q87" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q87" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q87" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
88. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Believe that criminals should receive help rather than punishment.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q88" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q88" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q88" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q88" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q88" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
89. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Value cooperation over competition.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q89" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q89" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q89" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q89" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q89" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
90. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Stick to my chosen path.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q90" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q90" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q90" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q90" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q90" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
91. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Get stressed out easily.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q91" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q91" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q91" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q91" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q91" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
92. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Act comfortably with others.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q92" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q92" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q92" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q92" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q92" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
93. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Like to get lost in thought.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q93" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q93" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q93" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q93" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q93" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
94. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Believe that people are basically moral.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q94" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q94" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q94" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q94" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q94" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
95. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Am sure of my ground.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q95" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q95" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q95" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q95" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q95" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
96. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Am often in a bad mood.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q96" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q96" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q96" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q96" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q96" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
97. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Involve others in what I am doing.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q97" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q97" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q97" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q97" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q97" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
98. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Love flowers.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q98" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q98" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q98" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q98" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q98" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
99. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Use others for my own ends.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q99" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q99" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q99" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q99" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q99" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
100. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Love order and regularity.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q100" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q100" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q100" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q100" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q100" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
101. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Have a low opinion of myself.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q101" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q101" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q101" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q101" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q101" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
102. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Seek to influence others.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q102" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q102" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q102" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q102" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q102" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
103. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Enjoy examining myself and my life.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q103" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q103" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q103" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q103" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q103" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
104. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Am concerned about others.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q104" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q104" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q104" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q104" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q104" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
105. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Tell the truth.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q105" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q105" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q105" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q105" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q105" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
106. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Am afraid to draw attention to myself.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q106" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q106" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q106" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q106" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q106" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
107. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Can manage many things at the same time.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q107" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q107" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q107" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q107" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q107" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
108. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Like to begin new things.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q108" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q108" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q108" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q108" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q108" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
109. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Have a sharp tongue.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q109" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q109" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q109" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q109" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q109" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
110. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Plunge into tasks with all my heart.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q110" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q110" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q110" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q110" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q110" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
111. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Go on binges.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q111" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q111" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q111" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q111" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q111" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
112. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Enjoy being part of a loud crowd.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q112" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q112" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q112" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q112" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q112" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
113. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Can handle a lot of information.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q113" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q113" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q113" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q113" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q113" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
114. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Seldom toot my own horn.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q114" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q114" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q114" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q114" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q114" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
115. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Get to work at once.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q115" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q115" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q115" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q115" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q115" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
116. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Can't make up my mind.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q116" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q116" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q116" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q116" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q116" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
117. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Laugh my way through life.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q117" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q117" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q117" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q117" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q117" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
118. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Believe in one true religion.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q118" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q118" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q118" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q118" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q118" VALUE="1"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
119. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Suffer from others' sorrows.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q119" VALUE="1"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q119" VALUE="2"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q119" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q119" VALUE="4"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q119" VALUE="5"></CENTER></TD>
</TR>
<TR><TD WIDTH="5%" VALIGN="TOP" HEIGHT=51>
120. </TD>
<TD WIDTH="28%" VALIGN="TOP" HEIGHT=51>
<P>Jump into things without thinking.</TD>
<TD WIDTH="14%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q120" VALUE="5"></CENTER></TD>
<TD WIDTH="13%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q120" VALUE="4"></CENTER></TD>
<TD WIDTH="17%" VALIGN="TOP" HEIGHT=51>
<CENTER>Neither Accurate<BR>
nor Inaccurate<BR>
<INPUT TYPE="RADIO" NAME="Q120" VALUE="3"></CENTER></TD>
<TD WIDTH="12%" VALIGN="TOP" HEIGHT=51>
<CENTER>Moderately<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q120" VALUE="2"></CENTER></TD>
<TD WIDTH="11%" VALIGN="TOP" HEIGHT=51>
<CENTER>Very<BR>
Accurate<BR>
<INPUT TYPE="RADIO" NAME="Q120" VALUE="1"></CENTER></TD>
</TR>

</table>

<p><br><input type="submit" value="Send "><b>&nbsp;&nbsp;This
will send your answers to be scored and take you to the next 60 questions.</b>
</form>
</body>
</html>
ENDOFTEXT
}
# Name:      random_password()
#
# Author:    Chris Hunt
#
# Date:      May 1999
#
# Purpose:   Returns a random word for use as a password. Consonants and vowels
#            are alternated to give a (hopefully) pronouncable, and hence
#            memorable, result.
#
# Arguments: The single (optional) argument sets the approximate length of the
#            word. Use of dipthongs (two-letter combinations) may make the word
#            exceed this length by 1. If the argument is omitted, a default
#            value (6) is assumed.
#
# Usage:     $my_new_password  = &random_password();
#            $my_long_password = &random_password(10);
#
# (c)1999 Chris Hunt. Permission is freely granted to include this script in
# your programs. provided this header is left intact.
#
# The latest version of this script can be found at http://www.extracon.com
#

sub random_password {

   ($maxlen) = $_[0] || 6;   # Default to 6

   # Build tables of vowels & consonants. Single vowels are repeated so that
   # resultant words are not dominated by dipthongs

   (@vowel) = ("a", "a", "a", "e", "e", "e", "e", "i", "i", "i",
          "o", "o", "o", "u", "u", "y", "ai", "au", "ay", "ea",
          "ee", "eu", "ia", "ie", "io", "oa", "oi", "oo", "oy");
   (@consonant) = ("b", "c", "d", "f", "g", "h", "j", "k", "l",
          "m", "n", "p", "qu", "r", "s", "t", "v", "w", "x", "z", "th", "st",
          "sh", "ph", "ng", "nd");
   ($password) = "";

   srand;
   ($vowelnext) = int(rand(2));  # Initialise to 0 or 1 (ie true or false)

   do {
      if ($vowelnext) {
         $password .= $vowel[rand(@vowel)];
      } else {
         $password .= $consonant[rand(@consonant)];
      }

      $vowelnext = !$vowelnext;    # Swap letter type for the next one

   } until length($password) >= $maxlen;

   return $password;

}
