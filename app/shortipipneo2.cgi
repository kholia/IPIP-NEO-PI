#!/usr/bin/env perl

# require("cgi-lib.pl");
use CGI qw(:cgi-lib);

MAIN:
{
# Read in identifying information
  &ReadParse(*input);

# Print the header
  print "Content-type: text/html\n\n";
  print "<!DOCTYPE html>\n";
  print "<HTML><HEAD>\n";
  print "<title>IPIP-NEO-PI Short Form Items 61-120</title>\n";
  print <<ENDOFTEXT;
<style type="text/css">
td { text-align: center;}
#main td:nth-child(1) { text-align: left;}
#main td:nth-child(2) { text-align: left;}

#main td:nth-child(2) { width: 28%;}
#main td:nth-child(3) { width: 14%;}
#main td:nth-child(4) { width: 13%;}
#main td:nth-child(5) { width: 17%;}
#main td:nth-child(6) { width: 12%;}

</style>
ENDOFTEXT

  print "</HEAD><Body><p>\n";

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

  print <<ENDOFTEXT;

  <form method=post action="shortipipneo3.cgi">
ENDOFTEXT

  print "<input type=\"hidden\" name=\"Nick\" value=\"$Nick\">\n";
  print "<input type=\"hidden\" name=\"Sex\" value=\"$Sex\">\n";
  print "<input type=\"hidden\" name=\"Age\" value=\"$Age\">\n";
  print "<input type=\"hidden\" name=\"Country\" value=\"$Country\">\n";
  for ($i = 1; $i < 61; $i++) {
  print "<input type=\"hidden\" name=\"Q$i\" value=\"$Q[$i]\">\n";
}
  print <<ENDOFTEXT;

<table border id="main">
<TR><TD>
<P>61. </TD>
<TD>
<P>Am afraid of many things.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q61" VALUE="1">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q61" VALUE="2">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q61" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q61" VALUE="4">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q61" VALUE="5">
</td>
</TR>
<TR><TD>
<P>62. </TD>
<TD>
<P>Avoid contacts with others.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q62" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q62" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q62" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q62" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q62" VALUE="1">
</td>
</TR>
<TR><TD>
<P>63. </TD>
<TD>
<P>Love to daydream.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q63" VALUE="1">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q63" VALUE="2">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q63" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q63" VALUE="4">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q63" VALUE="5">
</td>
</TR>
<TR><TD>
<P>64. </TD>
<TD>
<P>Trust what people say.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q64" VALUE="1">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q64" VALUE="2">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q64" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q64" VALUE="4">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q64" VALUE="5">
</td>
</TR>
<TR><TD>
<P>65. </TD>
<TD>
<P>Handle tasks smoothly.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q65" VALUE="1">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q65" VALUE="2">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q65" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q65" VALUE="4">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q65" VALUE="5">
</td>
</TR>
<TR><TD>
<P>66. </TD>
<TD>
<P>Lose my temper.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q66" VALUE="1">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q66" VALUE="2">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q66" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q66" VALUE="4">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q66" VALUE="5">
</td>
</TR>
<TR><TD>
<P>67. </TD>
<TD>
<P>Prefer to be alone.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q67" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q67" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q67" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q67" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q67" VALUE="1">
</td>
</TR>
<TR><TD>
<P>68. </TD>
<TD>
<P>Do not like poetry.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q68" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q68" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q68" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q68" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q68" VALUE="1">
</td>
</TR>
<TR><TD>
<P>69. </TD>
<TD>
<P>Take advantage of others.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q69" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q69" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q69" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q69" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q69" VALUE="1">
</td>
</TR>
<TR><TD>
<P>70. </TD>
<TD>
<P>Leave a mess in my room.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q70" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q70" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q70" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q70" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q70" VALUE="1">
</td>
</TR>
<TR><TD>
<P>71. </TD>
<TD>
<P>Am often down in the dumps.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q71" VALUE="1">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q71" VALUE="2">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q71" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q71" VALUE="4">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q71" VALUE="5">
</td>
</TR>
<TR><TD>
<P>72. </TD>
<TD>
<P>Take control of things.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q72" VALUE="1">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q72" VALUE="2">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q72" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q72" VALUE="4">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q72" VALUE="5">
</td>
</TR>
<TR><TD>
<P>73. </TD>
<TD>
<P>Rarely notice my emotional reactions.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q73" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q73" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q73" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q73" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q73" VALUE="1">
</td>
</TR>
<TR><TD>
<P>74. </TD>
<TD>
<P>Am indifferent to the feelings of others.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q74" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q74" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q74" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q74" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q74" VALUE="1">
</td>
</TR>
<TR><TD>
<P>75. </TD>
<TD>
<P>Break rules.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q75" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q75" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q75" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q75" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q75" VALUE="1">
</td>
</TR>
<TR><TD>
<P>76. </TD>
<TD>
<P>Only feel comfortable with friends.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q76" VALUE="1">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q76" VALUE="2">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q76" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q76" VALUE="4">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q76" VALUE="5">
</td>
</TR>
<TR><TD>
<P>77. </TD>
<TD>
<P>Do a lot in my spare time.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q77" VALUE="1">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q77" VALUE="2">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q77" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q77" VALUE="4">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q77" VALUE="5">
</td>
</TR>
<TR><TD>
<P>78. </TD>
<TD>
<P>Dislike changes.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q78" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q78" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q78" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q78" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q78" VALUE="1">
</td>
</TR>
<TR><TD>
<P>79. </TD>
<TD>
<P>Insult people.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q79" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q79" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q79" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q79" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q79" VALUE="1">
</td>
</TR>
<TR><TD>
<P>80. </TD>
<TD>
<P>Do just enough work to get by.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q80" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q80" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q80" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q80" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q80" VALUE="1">
</td>
</TR>
<TR><TD>
<P>81. </TD>
<TD>
<P>Easily resist temptations.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q81" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q81" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q81" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q81" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q81" VALUE="1">
</td>
</TR>
<TR><TD>
<P>82. </TD>
<TD>
<P>Enjoy being reckless.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q82" VALUE="1">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q82" VALUE="2">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q82" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q82" VALUE="4">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q82" VALUE="5">
</td>
</TR>
<TR><TD>
<P>83. </TD>
<TD>
<P>Have difficulty understanding abstract ideas.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q83" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q83" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q83" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q83" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q83" VALUE="1">
</td>
</TR>
<TR><TD>
<P>84. </TD>
<TD>
<P>Have a high opinion of myself.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q84" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q84" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q84" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q84" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q84" VALUE="1">
</td>
</TR>
<TR><TD>
<P>85. </TD>
<TD>
<P>Waste my time.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q85" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q85" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q85" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q85" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q85" VALUE="1">
</td>
</TR>
<TR><TD>
<P>86. </TD>
<TD>
<P>Feel that I'm unable to deal with things.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q86" VALUE="1">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q86" VALUE="2">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q86" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q86" VALUE="4">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q86" VALUE="5">
</td>
</TR>
<TR><TD>
<P>87. </TD>
<TD>
<P>Love life.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q87" VALUE="1">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q87" VALUE="2">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q87" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q87" VALUE="4">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q87" VALUE="5">
</td>
</TR>
<TR><TD>
<P>88. </TD>
<TD>
<P>Tend to vote for conservative political candidates.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q88" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q88" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q88" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q88" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q88" VALUE="1">
</td>
</TR>
<TR><TD>
<P>89. </TD>
<TD>
<P>Am not interested in other people's problems.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q89" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q89" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q89" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q89" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q89" VALUE="1">
</td>
</TR>
<TR><TD>
<P>90. </TD>
<TD>
<P>Rush into things.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q90" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q90" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q90" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q90" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q90" VALUE="1">
</td>
</TR>
<TR><TD>
<P>91. </TD>
<TD>
<P>Get stressed out easily.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q91" VALUE="1">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q91" VALUE="2">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q91" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q91" VALUE="4">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q91" VALUE="5">
</td>
</TR>
<TR><TD>
<P>92. </TD>
<TD>
<P>Keep others at a distance.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q92" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q92" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q92" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q92" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q92" VALUE="1">
</td>
</TR>
<TR><TD>
<P>93. </TD>
<TD>
<P>Like to get lost in thought.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q93" VALUE="1">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q93" VALUE="2">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q93" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q93" VALUE="4">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q93" VALUE="5">
</td>
</TR>
<TR><TD>
<P>94. </TD>
<TD>
<P>Distrust people.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q94" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q94" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q94" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q94" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q94" VALUE="1">
</td>
</TR>
<TR><TD>
<P>95. </TD>
<TD>
<P>Know how to get things done.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q95" VALUE="1">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q95" VALUE="2">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q95" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q95" VALUE="4">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q95" VALUE="5">
</td>
</TR>
<TR><TD>
<P>96. </TD>
<TD>
<P>Am not easily annoyed.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q96" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q96" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q96" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q96" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q96" VALUE="1">
</td>
</TR>
<TR><TD>
<P>97. </TD>
<TD>
<P>Avoid crowds.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q97" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q97" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q97" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q97" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q97" VALUE="1">
</td>
</TR>
<TR><TD>
<P>98. </TD>
<TD>
<P>Do not enjoy going to art museums.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q98" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q98" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q98" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q98" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q98" VALUE="1">
</td>
</TR>
<TR><TD>
<P>99. </TD>
<TD>
<P>Obstruct others' plans.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q99" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q99" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q99" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q99" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q99" VALUE="1">
</td>
</TR>
<TR><TD>
<P>100. </TD>
<TD>
<P>Leave my belongings around.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q100" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q100" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q100" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q100" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q100" VALUE="1">
</td>
</TR>
<TR><TD>
<P>101. </TD>
<TD>
<P>Feel comfortable with myself.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q101" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q101" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q101" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q101" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q101" VALUE="1">
</td>
</TR>
<TR><TD>
<P>102. </TD>
<TD>
<P>Wait for others to lead the way.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q102" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q102" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q102" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q102" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q102" VALUE="1">
</td>
</TR>
<TR><TD>
<P>103. </TD>
<TD>
<P>Don't understand people who get emotional.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q103" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q103" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q103" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q103" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q103" VALUE="1">
</td>
</TR>
<TR><TD>
<P>104. </TD>
<TD>
<P>Take no time for others.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q104" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q104" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q104" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q104" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q104" VALUE="1">
</td>
</TR>
<TR><TD>
<P>105. </TD>
<TD>
<P>Break my promises.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q105" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q105" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q105" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q105" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q105" VALUE="1">
</td>
</TR>
<TR><TD>
<P>106. </TD>
<TD>
<P>Am not bothered by difficult social situations.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q106" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q106" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q106" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q106" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q106" VALUE="1">
</td>
</TR>
<TR><TD>
<P>107. </TD>
<TD>
<P>Like to take it easy.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q107" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q107" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q107" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q107" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q107" VALUE="1">
</td>
</TR>
<TR><TD>
<P>108. </TD>
<TD>
<P>Am attached to conventional ways.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q108" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q108" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q108" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q108" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q108" VALUE="1">
</td>
</TR>
<TR><TD>
<P>109. </TD>
<TD>
<P>Get back at others.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q109" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q109" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q109" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q109" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q109" VALUE="1">
</td>
</TR>
<TR><TD>
<P>110. </TD>
<TD>
<P>Put little time and effort into my work.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q110" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q110" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q110" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q110" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q110" VALUE="1">
</td>
</TR>
<TR><TD>
<P>111. </TD>
<TD>
<P>Am able to control my cravings.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q111" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q111" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q111" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q111" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q111" VALUE="1">
</td>
</TR>
<TR><TD>
<P>112. </TD>
<TD>
<P>Act wild and crazy.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q112" VALUE="1">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q112" VALUE="2">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q112" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q112" VALUE="4">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q112" VALUE="5">
</td>
</TR>
<TR><TD>
<P>113. </TD>
<TD>
<P>Am not interested in theoretical discussions.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q113" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q113" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q113" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q113" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q113" VALUE="1">
</td>
</TR>
<TR><TD>
<P>114. </TD>
<TD>
<P>Boast about my virtues.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q114" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q114" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q114" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q114" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q114" VALUE="1">
</td>
</TR>
<TR><TD>
<P>115. </TD>
<TD>
<P>Have difficulty starting tasks.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q115" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q115" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q115" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q115" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q115" VALUE="1">
</td>
</TR>
<TR><TD>
<P>116. </TD>
<TD>
<P>Remain calm under pressure.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q116" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q116" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q116" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q116" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q116" VALUE="1">
</td>
</TR>
<TR><TD>
<P>117. </TD>
<TD>
<P>Look at the bright side of life.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q117" VALUE="1">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q117" VALUE="2">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q117" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q117" VALUE="4">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q117" VALUE="5">
</td>
</TR>
<TR><TD>
<P>118. </TD>
<TD>
<P>Believe that we should be tough on crime.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q118" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q118" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q118" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q118" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q118" VALUE="1">
</td>
</TR>
<TR><TD>
<P>119. </TD>
<TD>
<P>Try not to think about the needy.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q119" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q119" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q119" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q119" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q119" VALUE="1">
</td>
</TR>
<TR><TD>
<P>120. </TD>
<TD>
<P>Act without thinking.</TD>
<TD>
Very<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q120" VALUE="5">
</td>
<TD>
Moderately<BR>
Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q120" VALUE="4">
</td>
<TD>
Neither Accurate<BR>
nor Inaccurate<BR>

<INPUT TYPE="RADIO" NAME="Q120" VALUE="3">
</td>
<TD>
Moderately<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q120" VALUE="2">
</td>
<TD>
Very<BR>
Accurate<BR>

<INPUT TYPE="RADIO" NAME="Q120" VALUE="1">
</td>
</TR>
</TABLE>

<p><b>PLEASE NOTE:</b> Your results should appear on your screen within moments after clicking the Send button. If nothing happens, something has gone wrong. Clicking the button again and again will not help.</p>
<p>
As I indicated in the warning at the beginning of the test, I am a psychologist, not a computer technician, so I have no definitive way of solving any person's particular computer problem.  For people who were unable to complete the test, sometimes using a better computer, faster internet connection, or just taking the test on a different day and time led to success. If you experience difficulties, you can email me if you like (j5j at psu.edu), but I won't be able to tell you anything more than what I have just said here.</p>
<p><br><input type="submit" value="Send "><b>&nbsp;&nbsp;This
will send your answers to be scored and post your results.</b>
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
