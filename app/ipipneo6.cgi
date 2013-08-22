#!/usr/bin/env perl

use CGI qw(:cgi-lib);
# require("cgi-lib.pl");

MAIN:
{
# Print the header
  print &PrintHeader;
  print &HtmlTop ("IPIP-NEO Narrative Report");

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
  ($Q[241] = $input{'Q241'});
  ($Q[242] = $input{'Q242'});
  ($Q[243] = $input{'Q243'});
  ($Q[244] = $input{'Q244'});
  ($Q[245] = $input{'Q245'});
  ($Q[246] = $input{'Q246'});
  ($Q[247] = $input{'Q247'});
  ($Q[248] = $input{'Q248'});
  ($Q[249] = $input{'Q249'});
  ($Q[250] = $input{'Q250'});
  ($Q[251] = $input{'Q251'});
  ($Q[252] = $input{'Q252'});
  ($Q[253] = $input{'Q253'});
  ($Q[254] = $input{'Q254'});
  ($Q[255] = $input{'Q255'});
  ($Q[256] = $input{'Q256'});
  ($Q[257] = $input{'Q257'});
  ($Q[258] = $input{'Q258'});
  ($Q[259] = $input{'Q259'});
  ($Q[260] = $input{'Q260'});
  ($Q[261] = $input{'Q261'});
  ($Q[262] = $input{'Q262'});
  ($Q[263] = $input{'Q263'});
  ($Q[264] = $input{'Q264'});
  ($Q[265] = $input{'Q265'});
  ($Q[266] = $input{'Q266'});
  ($Q[267] = $input{'Q267'});
  ($Q[268] = $input{'Q268'});
  ($Q[269] = $input{'Q269'});
  ($Q[270] = $input{'Q270'});
  ($Q[271] = $input{'Q271'});
  ($Q[272] = $input{'Q272'});
  ($Q[273] = $input{'Q273'});
  ($Q[274] = $input{'Q274'});
  ($Q[275] = $input{'Q275'});
  ($Q[276] = $input{'Q276'});
  ($Q[277] = $input{'Q277'});
  ($Q[278] = $input{'Q278'});
  ($Q[279] = $input{'Q279'});
  ($Q[280] = $input{'Q280'});
  ($Q[281] = $input{'Q281'});
  ($Q[282] = $input{'Q282'});
  ($Q[283] = $input{'Q283'});
  ($Q[284] = $input{'Q284'});
  ($Q[285] = $input{'Q285'});
  ($Q[286] = $input{'Q286'});
  ($Q[287] = $input{'Q287'});
  ($Q[288] = $input{'Q288'});
  ($Q[289] = $input{'Q289'});
  ($Q[290] = $input{'Q290'});
  ($Q[291] = $input{'Q291'});
  ($Q[292] = $input{'Q292'});
  ($Q[293] = $input{'Q293'});
  ($Q[294] = $input{'Q294'});
  ($Q[295] = $input{'Q295'});
  ($Q[296] = $input{'Q296'});
  ($Q[297] = $input{'Q297'});
  ($Q[298] = $input{'Q298'});
  ($Q[299] = $input{'Q299'});
  ($Q[300] = $input{'Q300'});
  ($V1 = $input{'A'});
  ($V2 = $input{'B'});
  ($V3 = $input{'C'});

# Score facet scales
  for ($i = 1; $i < 31; $i++) {
    $k = 0;
    for ($j = 0; $j < 10; $j++) {
    ($ss[$i] += $Q[$i+$k]);
    ($k += 30);
}
}

# Number each facet set from 1-6

  ($j = 0);
  for ($i = 1; $i < 7; $i++) {
  ($NF[$i] = $ss[$i + $j]);
  ($EF[$i] = $ss[$i + $j + 1]);
  ($OF[$i] = $ss[$i + $j + 2]);
  ($AF[$i] = $ss[$i + $j + 3]);
  ($CF[$i] = $ss[$i + $j + 4]);
  ($j += 4);
}

# Score domain scales
#          1         2          3         4         5         6
  ($N = $ss[1] + $ss[6]  + $ss[11] + $ss[16] + $ss[21] + $ss[26]);
  ($E = $ss[2] + $ss[7]  + $ss[12] + $ss[17] + $ss[22] + $ss[27]);
  ($O = $ss[3] + $ss[8]  + $ss[13] + $ss[18] + $ss[23] + $ss[28]);
  ($A = $ss[4] + $ss[9]  + $ss[14] + $ss[19] + $ss[24] + $ss[29]);
  ($C = $ss[5] + $ss[10] + $ss[15] + $ss[20] + $ss[25] + $ss[30]);

# Standardize scores

  if ($Sex eq "Male" && $Age < 21) {
@norm = (0,164.2,197.6,217.8,197.1,204.2,33.4,34.2,28.1,28.0,29.1,
     27.9,26.8,26.2,29.4,29.9,24.1,7.7,8.3,9.2,7.4,6.4,6.3,
     33.9,29.8,34.0,29.6,33.9,36.5,8.0,8.9,7.4,5.6,8.1,7.1,
     40.6,37.3,36.1,35.7,39.6,28.5,6.8,7.0,6.8,6.4,7.1,8.0,
     32.5,34.7,37.5,31.2,28.1,33.2,7.6,6.7,6.6,6.9,7.1,6.5,
     38.3,30.5,38.1,36.2,29.2,31.9,5.6,7.7,5.9,6.7,8.0,7.2);
  ($id = "men of traditional college age");
}

  if ($Sex eq "Male" && $Age > 20) {
@norm = (0,161.8,192.8,218.4,202.8,215.3,38.7,31.9,26.6,27.3,30.8,
     27.6,27.0,25.6,27.8,31.1,22.6,8.0,9.3,9.8,7.6,7.3,7.4,
     33.1,27.3,34.6,30.6,30.8,36.4,8.1,8.1,7.5,6.0,7.6,7.0,
     39.1,38.3,35.4,35.8,40.9,28.8,6.6,6.8,6.7,6.6,6.7,8.1,
     33.6,36.2,37.6,33.7,28.5,33.2,7.6,6.4,6.4,6.9,6.9,6.8,
     39.7,33.0,39.7,38.2,31.3,33.4,5.7,7.8,5.8,6.7,8.4,7.3);
  ($id = "adult men");
}

  if ($Sex eq "Female" && $Age < 21) {
@norm = (0,180.0,203.9,228.7,208.6,203.5,37.5,35.0,26.8,29.1,31.0,
     31.3,29.8,27.9,30.6,29.9,27.6,7.9,9.1,9.6,7.7,6.4,7.6,
     34.8,31.7,34.0,30.5,34.0,38.9,8.5,9.2,8.1,5.6,8.2,7.0,
     41.5,42.5,39.4,36.3,39.0,30.0,6.9,5.7,6.5,6.3,7.1,7.2,
     33.9,37.4,39.5,32.5,29.9,35.4,7.4,6.1,6.5,7.6,7.0,6.7,
     37.6,30.6,38.9,37.2,29.0,30.2,5.8,8.3,6.0,7.0,8.0,7.7);
  ($id = "women of traditional college age");
}

   if ($Sex eq "Female" && $Age > 20) {
@norm = (0,172.5,196.2,226.3,217.3,220.7,36.8,31.7,26.8,25.3,29.8,
     30.7,28.8,26.5,29.1,31.1,25.3,7.8,8.8,9.4,7.5,7.3,7.5,
     35.1,28.5,34.2,32.0,28.6,37.8,8.1,8.5,7.4,5.9,7.8,6.9,
     38.5,42.3,39.4,35.9,39.8,30.3,7.4,5.7,6.2,6.7,7.0,7.5,
     34.5,39.6,40.5,35.5,31.0,36.3,7.4,5.7,5.9,6.8,6.7,6.3,
     39.9,34.1,41.5,39.4,32.6,33.3,5.6,8.5,5.4,6.2,8.3,7.3);
  ($id = "adult women");
}

  ($SN =  (10 * ($N - $norm[1])/$norm[6]) + 50);
  ($SE =  (10 * ($E - $norm[2])/$norm[7]) + 50);
  ($SO =  (10 * ($O - $norm[3])/$norm[8]) + 50);
  ($SA =  (10 * ($A - $norm[4])/$norm[9]) + 50);
  ($SC =  (10 * ($C - $norm[5])/$norm[10]) + 50);

  for ($i = 1; $i < 7; $i++) {
    ($SNF[$i] = 50 + (10 * ($NF[$i]-$norm[$i + 10])/$norm[$i + 16]));
    ($SEF[$i] = 50 + (10 * ($EF[$i]-$norm[$i + 22])/$norm[$i + 28]));
    ($SOF[$i] = 50 + (10 * ($OF[$i]-$norm[$i + 34])/$norm[$i + 40]));
    ($SAF[$i] = 50 + (10 * ($AF[$i]-$norm[$i + 46])/$norm[$i + 52]));
    ($SCF[$i] = 50 + (10 * ($CF[$i]-$norm[$i + 58])/$norm[$i + 64]));
}


# Cubic approximations for percentiles

  ($SNP = int(210.335958661391 - (16.7379362643389 * $SN) + (0.405936512733332 * $SN ** 2) - (0.00270624341822222 * $SN ** 3)));
  ($SEP = int(210.335958661391 - (16.7379362643389 * $SE) + (0.405936512733332 * $SE ** 2) - (0.00270624341822222 * $SE ** 3)));
  ($SOP = int(210.335958661391 - (16.7379362643389 * $SO) + (0.405936512733332 * $SO ** 2) - (0.00270624341822222 * $SO ** 3)));
  ($SAP = int(210.335958661391 - (16.7379362643389 * $SA) + (0.405936512733332 * $SA ** 2) - (0.00270624341822222 * $SA ** 3)));
  ($SCP = int(210.335958661391 - (16.7379362643389 * $SC) + (0.405936512733332 * $SC ** 2) - (0.00270624341822222 * $SC ** 3)));

  if ($SN < 27) {$SNP = 1};
  if ($SE < 27) {$SEP = 1};
  if ($SO < 27) {$SOP = 1};
  if ($SA < 27) {$SAP = 1};
  if ($SC < 27) {$SCP = 1};

  if ($SN > 73) {$SNP = 99};
  if ($SE > 73) {$SEP = 99};
  if ($SO > 73) {$SOP = 99};
  if ($SA > 73) {$SAP = 99};
  if ($SC > 73) {$SCP = 99};

# Create percentile scores and low, average, high labels for facets

  for ($i = 1; $i < 7; $i++) {
    $fflev[$i] = $SNF[$i];
    if ($SNF[$i] < 45) {
      ($flev[$i] = "low");
}
    if ($SNF[$i] >= 45 && $SNF[$i] <= 55) {
      ($flev[$i] = "average");
}
    if ($SNF[$i] > 55) {
      ($flev[$i] = "high");
}
  ($SNFP[$i] = int(210.335958661391 - (16.7379362643389 * $SNF[$i]) + (0.405936512733332 * $SNF[$i] ** 2) - (0.00270624341822222 * $SNF[$i] ** 3)));
  if ($SNF[$i] < 27) {$SNFP[$i] = 1};
  if ($SNF[$i] > 73) {$SNFP[$i] = 99};
}
  for ($i = 1; $i < 7; $i++) {
    $fflev[$i + 6] = $SEF[$i];
    if ($SEF[$i] < 45) {
      ($flev[$i + 6] = "low");
}
    if ($SEF[$i] >= 45 && $SEF[$i] <= 55) {
      ($flev[$i + 6] = "average");
}
    if ($SEF[$i] > 55) {
      ($flev[$i + 6] = "high");
}
  ($SEFP[$i] = int(210.335958661391 - (16.7379362643389 * $SEF[$i]) + (0.405936512733332 * $SEF[$i] ** 2) - (0.00270624341822222 * $SEF[$i] ** 3)));
  if ($SEF[$i] < 27) {$SEFP[$i] = 1};
  if ($SEF[$i] > 73) {$SEFP[$i] = 99};
}

  for ($i = 1; $i < 7; $i++) {
    $fflev[$i + 12] = $SOF[$i];
    if ($SOF[$i] < 45) {
      ($flev[$i + 12] = "low");
}
    if ($SOF[$i] >= 45 && $SOF[$i] <= 55) {
      ($flev[$i + 12] = "average");
}
    if ($SOF[$i] > 55) {
      ($flev[$i + 12] = "high");
}
  ($SOFP[$i] = int(210.335958661391 - (16.7379362643389 * $SOF[$i]) + (0.405936512733332 * $SOF[$i] ** 2) - (0.00270624341822222 * $SOF[$i] ** 3)));
  if ($SOF[$i] < 27) {$SOFP[$i] = 1};
  if ($SOF[$i] > 73) {$SOFP[$i] = 99};
}

  for ($i = 1; $i < 7; $i++) {
    $fflev[$i + 18] = $SAF[$i];
    if ($SAF[$i] < 45) {
      ($flev[$i + 18] = "low");
}
    if ($SAF[$i] >= 45 && $SAF[$i] <= 55) {
      ($flev[$i + 18] = "average");
}
    if ($SAF[$i] > 55) {
      ($flev[$i + 18] = "high");
}
  ($SAFP[$i] = int(210.335958661391 - (16.7379362643389 * $SAF[$i]) + (0.405936512733332 * $SAF[$i] ** 2) - (0.00270624341822222 * $SAF[$i] ** 3)));
  if ($SAF[$i] < 27) {$SAFP[$i] = 1};
  if ($SAF[$i] > 73) {$SAFP[$i] = 99};
}

  for ($i = 1; $i < 7; $i++) {
    $fflev[$i + 24] = $SCF[$i];
    if ($SCF[$i] < 45) {
      ($flev[$i + 24] = "low");
}
    if ($SCF[$i] >= 45 && $SCF[$i] <= 55) {
      ($flev[$i + 24] = "average");
}
    if ($SCF[$i] > 55) {
      ($flev[$i + 24] = "high");
}
  ($SCFP[$i] = int(210.335958661391 - (16.7379362643389 * $SCF[$i]) + (0.405936512733332 * $SCF[$i] ** 2) - (0.00270624341822222 * $SCF[$i] ** 3)));
  if ($SCF[$i] < 27) {$SCFP[$i] = 1};
  if ($SCF[$i] > 73) {$SCFP[$i] = 99};
}

#Create graphs

  $ASTERISK = '*';

  $GRPHHEAD[0] = 'Domain/Facet...........';
  $GRPHHEAD[1] = 'Score';

  $EL1 = "EXTRAVERSION...............$SEP ";
  $EL2 = "..Friendliness.............$SEFP[1] ";
  $EL3 = "..Gregariousness...........$SEFP[2] ";
  $EL4 = "..Assertiveness............$SEFP[3] ";
  $EL5 = "..Activity Level...........$SEFP[4] ";
  $EL6 = "..Excitement-Seeking.......$SEFP[5] ";
  $EL7 = "..Cheerfulness.............$SEFP[6] ";

  ($WEP = 4.1 * $SEP);
 for ($i = 0; $i < 7; $i++) {
    ($WE[$i] = (4.1 * $SEFP[$i]));
}


  $AL1 = "AGREEABLENESS..............$SAP ";
  $AL2 = "..Trust....................$SAFP[1] ";
  $AL3 = "..Morality.................$SAFP[2] ";
  $AL4 = "..Altruism.................$SAFP[3] ";
  $AL5 = "..Cooperation..............$SAFP[4] ";
  $AL6 = "..Modesty..................$SAFP[5] ";
  $AL7 = "..Sympathy.................$SAFP[6] ";

  ($WAP = 4.1 * $SAP);
 for ($i = 0; $i < 7; $i++) {
    ($WA[$i] = (4.1 * $SAFP[$i]));
}

  $CL1 = "CONSCIENTIOUSNESS..........$SCP ";
  $CL2 = "..Self-Efficacy............$SCFP[1] ";
  $CL3 = "..Orderliness..............$SCFP[2] ";
  $CL4 = "..Dutifulness..............$SCFP[3] ";
  $CL5 = "..Achievement-Striving.....$SCFP[4] ";
  $CL6 = "..Self-Discipline..........$SCFP[5] ";
  $CL7 = "..Cautiousness.............$SCFP[6] ";

  ($WCP = 4.1 * $SCP);
 for ($i = 0; $i < 7; $i++) {
    ($WC[$i] = (4.1 * $SCFP[$i]));
}

  $NL1 = "NEUROTICISM................$SNP ";
  $NL2 = "..Anxiety..................$SNFP[1] ";
  $NL3 = "..Anger....................$SNFP[2] ";
  $NL4 = "..Depression...............$SNFP[3] ";
  $NL5 = "..Self-Consciousness.......$SNFP[4] ";
  $NL6 = "..Immoderation.............$SNFP[5] ";
  $NL7 = "..Vulnerability............$SNFP[6] ";

  ($WNP = 4.1 * $SNP);
 for ($i = 0; $i < 7; $i++) {
    ($WN[$i] = (4.1 * $SNFP[$i]));
}

  $OL1 = "OPENNESS TO EXPERIENCE.....$SOP ";
  $OL2 = "..Imagination..............$SOFP[1] ";
  $OL3 = "..Artistic Interests.......$SOFP[2] ";
  $OL4 = "..Emotionality.............$SOFP[3] ";
  $OL5 = "..Adventurousness..........$SOFP[4] ";
  $OL6 = "..Intellect................$SOFP[5] ";
  $OL7 = "..Liberalism...............$SOFP[6] ";

  ($WOP = 4.1 * $SOP);
 for ($i = 0; $i < 7; $i++) {
    ($WO[$i] = (4.1 * $SOFP[$i]));
}


#Create lines of item responses
for ($i = 0; $i < 60; $i++) {
  $line1[$i] = $Q[$i + 1];
  $line2[$i] = $Q[$i + 61];
  $line3[$i] = $Q[$i + 121];
  $line4[$i] = $Q[$i + 181];
  $line5[$i] = $Q[$i + 241];
}

# Create gender variable

  if ($Sex eq "Male") {
$Gender = 1;
}
  if ($Sex eq "Female") {
$Gender = 2;
}

#Get time
$t = time();
($sec,$min,$hour,$dom,$mon,$year,$wday,$yday,$isdst) = localtime($t);

#Check sex and age
  if ($Sex ne "Male" && $Sex ne "Female") {
    print <<ENDOFTEXT;

You did not indicate your sex at the beginning of the inventory. Your answers
cannot be normed properly unless you indicate whether you are male or female.
Please return to the inventory and indicate your sex.
ENDOFTEXT
  exit;
}
  if ($Age < 10) {
    print <<ENDOFTEXT;

You did not indicate how old you are at the beginning of the inventory, or you
typed in an age that is too young. Your answers cannot be normed properly
unless type in a valid age. Please return to the inventory and change your response.
ENDOFTEXT
  exit;
}

  print <<ENDOFTEXT;
<basefont = 3>
<font = +1><B>NOTE: The report sent to your computer screen upon the completion of the IPIP-NEO is only a temporary web page. When you exit your web browser you will not be able to return to this URL to re-access your report. No copies of the report are sent to anyone. IF YOU WANT A PERMANENT COPY OF THE REPORT, YOU MUST SAVE THE WEB PAGE TO YOUR HARD DRIVE OR OTHER STORAGE MEDIUM, AND/OR PRINT THE REPORT WHILE YOU ARE STILL VIEWING IT IN YOUR WEB BROWSER. Probably the best way to save the report is to select and copy the entire page (Ctrl-A, Ctrl-C on most browsers), paste it into a word processor, and save the document. </b></font><p><p>

This report compares $Nick from the country $Country to other $id.<P><p>

This report estimates the individual's level on each of the five broad  personality domains of the Five-Factor Model. The description of each one of the five broad domains is followed by a more detailed description of personality according to the six subdomains that comprise each domain.<p><p>

<I>A note on terminology</i>. Personality traits describe, relative to other people, the frequency or intensity of a person's feelings, thoughts, or behaviors. Possession of a trait is therefore a matter of degree. We might describe two individuals as <I>extraverts</i>, but still see one as more extraverted than the other. This report uses expressions such as "extravert" or "high in extraversion" to describe someone who is likely to be seen by others as relatively extraverted. The computer program that generates this report classifies you as low, average, or high in a trait according to whether your score is approximately in the lowest 30%, middle 40%, or highest 30% of scores obtained by people of your sex and roughly your age. Your numerical scores are reported and graphed as <I>percentile estimates</i>. For example, a score of "60" means that your level on that trait is estimated to be higher than 60% of persons of your sex and age.<p><p>

Please keep in mind that "low," "average," and "high" scores on a personality test are neither absolutely good nor bad. A particular level on any trait will probably be neutral or irrelevant for a great many activites, be helpful for accomplishing some things, and detrimental for accomplishing other things.

As with any personality inventory, scores and descriptions can only approximate an individual's actual personality. High and low score descriptions are usually accurate, but average scores close to the low or high boundaries might misclassify you as only average. On each set of six subdomain scales it is somewhat uncommon but certainly possible to score high in some of the subdomains and low in the others. In such cases more attention should be paid to the subdomain scores than to the broad domain score. Questions about the accuracy of your results are best resolved by showing your report to people who know you well.<p><p>

John A. Johnson wrote descriptions of the five domains and thirty subdomains. These descriptions are based on an extensive reading of the scientific literature on personality measurement. Although Dr. Johnson would like to be acknowledged as the author of these materials if they are reproduced, he has placed them in the public domain.
ENDOFTEXT

#Report based on low, average, or high scores
#Report based on low, average, or high scores

  ($LO = 45);
  ($HI = 55);

  print <<ENDOFTEXT;

<H2>Extraversion</h2>

Extraversion is marked by pronounced engagement with the external world. Extraverts enjoy being with people, are full of energy, and often experience
positive emotions. They tend to be enthusiastic, action-oriented, individuals who are likely to say "Yes!" or "Let's go!" to opportunities for excitement.
In groups they like to talk, assert themselves, and draw attention to
themselves.<p><p>

Introverts lack the exuberance, energy, and activity levels of extraverts. They tend to be quiet, low-key, deliberate, and disengaged from the social world. Their lack of social involvement should <U>not</u> be interpreted as shyness or depression; the introvert simply needs less stimulation than an extravert and prefers to be alone. The independence and reserve of the introvert is sometimes mistaken as unfriendliness or arrogance. In reality, an introvert who scores high on the agreeableness dimension will not seek others out but will be quite pleasant when approached.<p><p>

<table>
<tr><td>DOMAIN/Facet</td><td>Score</td><td><img src='grphhead.jpg'></td></tr>
<tr><td>EXTRAVERSION</td><td>$SEP</td><td><img src='bargray.jpg' width=$WEP height='20'></td></tr>
<tr><td>..Friendliness</td><td>$SEFP[1]</td><td><img src='bargray.jpg' width=$WE[1] height='20'></td></tr>
<tr><td>..Gregariousness</td><td>$SEFP[2]</td><td><img src='bargray.jpg' width=$WE[2] height='20'></td></tr>
<tr><td>..Assertiveness</td><td>$SEFP[3]</td><td><img src='bargray.jpg' width=$WE[3] height='20'></td></tr>
<tr><td>..Activity Level</td><td>$SEFP[4]</td><td><img src='bargray.jpg' width=$WE[4] height='20'></td></tr>
<tr><td>..Excitement-Seeking</td><td>$SEFP[5]</td><td><img src='bargray.jpg' width=$WE[5] height='20'></td></tr>
<tr><td>..Cheerfulness</td><td>$SEFP[6]</td><td><img src='bargray.jpg' width=$WE[6] height='20'></td></tr>
</table>

ENDOFTEXT

  if ($SE < $LO) {
      print <<ENDOFTEXT;

Your score on Extraversion is low, indicating you are introverted, reserved, and quiet. You enjoy solitude and solitary activities. Your socializing tends to be restricted to a few close friends.<P><P>
ENDOFTEXT
}

  if ($SE >= $LO && $SE <= $HI) {
      print <<ENDOFTEXT;
Your score on Extraversion is average, indicating you are neither a subdued loner nor a jovial chatterbox. You enjoy time with others but also time alone.<P><P>
ENDOFTEXT
}


  if ($SE > $HI) {
      print <<ENDOFTEXT;
Your score on Extraversion is high, indicating you are sociable, outgoing, energetic, and lively. You prefer to be around people much of the time.<P><P>
ENDOFTEXT
}

  print <<ENDOFTEXT;

<H3>Extraversion Facets</h3>

<ul>
<li> <I>Friendliness</i>. Friendly people genuinely like other people and openly
     demonstrate positive feelings toward others. They make friends quickly
     and it is easy for them to form close, intimate relationships. Low scorers
     on Friendliness are not necessarily cold and hostile, but they do not reach
     out to others and are perceived as distant and reserved. Your level of
     friendliness is $flev[7].</li>
<li> <I>Gregariousness</i>. Gregarious people find the company of others
     pleasantly stimulating and rewarding. They enjoy the excitement of
     crowds. Low scorers tend to feel overwhelmed by, and therefore actively
     avoid, large crowds. They do not necessarily dislike being with people
     sometimes, but their need for privacy and time to themselves is much
     greater than for individuals who score high on this scale. Your level of
     gregariousness is $flev[8].</li>
<li> <I>Assertiveness</i>. High scorers Assertiveness like to speak out, take
     charge, and direct the activities of others. They tend to be leaders in
     groups. Low scorers tend not to talk much and let others control the
     activities of groups. Your level of assertiveness is $flev[9].</li>
<li> <I>Activity Level</i>. Active individuals lead fast-paced, busy lives. They
     move about quickly, energetically, and vigorously, and they are involved in
     many activities. People who score low on this scale follow a slower and
     more leisurely, relaxed pace. Your activity level is $flev[10].</li>
<li> <I>Excitement-Seeking</i>. High scorers on this scale are easily bored
     without high levels of stimulation. They love bright lights and hustle and
     bustle. They are likely to take risks and seek thrills. Low scorers are
     overwhelmed by noise and commotion and are adverse to thrill-seeking.
     Your level of excitement-seeking is $flev[11].</li>
<li> <I>Cheerfulness</i>. This scale measures positive mood and feelings, not
     negative emotions (which are a part of the Neuroticism domain). Persons who
     score high on this scale typically experience a range of positive feelings,
     including happiness, enthusiasm, optimism, and joy. Low scorers are not as
     prone to such energetic, high spirits. Your level of positive emotions is
     $flev[12].</li>
</ul>
ENDOFTEXT

  print <<ENDOFTEXT;

<H2>Agreeableness</h2>

Agreeableness reflects individual differences in concern with cooperation and
social harmony. Agreeable individuals value getting along with others. They are
therefore considerate, friendly, generous, helpful, and willing to compromise
their interests with others'. Agreeable people also have an optimistic view of
human nature. They believe people are basically honest, decent, and
trustworthy.<p><p>

Disagreeable individuals place self-interest above getting along with others.
They are generally unconcerned with others' well-being, and therefore are
unlikely to extend themselves for other people. Sometimes their skepticism about
others' motives causes them to be suspicious, unfriendly, and
uncooperative.<p><p>

Agreeableness is obviously advantageous for attaining and maintaining
popularity. Agreeable people are better liked than disagreeable people. On the
other hand, agreeableness is not useful in situations that require tough or
absolute objective decisions. Disagreeable people can make excellent scientists,
critics, or soldiers.<p><p>

<table>
<tr><td>DOMAIN/Facet</td><td>Score</td><td><img src='grphhead.jpg'></td></tr>
<tr><td>AGREEABLENESS</td><td>$SAP</td><td><img src='bargray.jpg' width=$WAP height='20'></td></tr>
<tr><td>..Trust</td><td>$SAFP[1]</td><td><img src='bargray.jpg' width=$WA[1] height='20'></td></tr>
<tr><td>..Morality</td><td>$SAFP[2]</td><td><img src='bargray.jpg' width=$WA[2] height='20'></td></tr>
<tr><td>..Altruism</td><td>$SAFP[3]</td><td><img src='bargray.jpg' width=$WA[3] height='20'></td></tr>
<tr><td>..Cooperation</td><td>$SAFP[4]</td><td><img src='bargray.jpg' width=$WA[4] height='20'></td></tr>
<tr><td>..Modesty</td><td>$SAFP[5]</td><td><img src='bargray.jpg' width=$WA[5] height='20'></td></tr>
<tr><td>..Sympathy</td><td>$SAFP[6]</td><td><img src='bargray.jpg' width=$WA[6] height='20'></td></tr>
</table>

ENDOFTEXT

  if ($SA < $LO) {
      print <<ENDOFTEXT;
Your score on Agreeableness is low, indicating less concern with others' needs
Than with your own. People see you as tough, critical, and uncompromising.<P><P>
ENDOFTEXT
}

  if ($SA >= $LO && $SA <= $HI) {
      print <<ENDOFTEXT;
Your level of Agreeableness is average, indicating some concern with others'
Needs, but, generally, unwillingness to sacrifice yourself for others.<P><P>
ENDOFTEXT
}

  if ($SA > $HI) {
      print <<ENDOFTEXT;
Your high level of Agreeableness indicates a strong interest in others' needs
and well-being. You are pleasant, sympathetic, and cooperative.<P><P>
ENDOFTEXT
}

  print <<ENDOFTEXT;

<H3>Agreeableness Facets</h3>

<ul>
<li> <I>Trust</i>. A person with high trust assumes that most people are
     fair, honest, and have good intentions. Persons low in trust see others
     as selfish, devious, and potentially dangerous. Your level of
     trust is $flev[19].</li>
<li> <I>Morality</i>. High scorers on this scale see no need for pretense
     or manipulation when dealing with others and are therefore candid, frank,
     and sincere. Low scorers believe that a certain amount of deception in
     social relationships is necessary. People find it relatively easy to relate
     to the straightforward high-scorers on this scale. They generally find it
     more difficult to relate to the unstraightforward low-scorers on this
     scale. It should be made clear that low scorers are <U>not</u> unprincipled
     or immoral; they are simply more guarded and less willing to openly reveal
     the whole truth. Your level of morality is $flev[20].</li>
<li> <I>Altruism</i>. Altruistic people find helping other people genuinely
     rewarding. Consequently, they are generally willing to assist those who
     are in need. Altruistic people find that doing things for others is a form
     of self-fulfillment rather than self-sacrifice. Low scorers on this scale
     do not particularly like helping those in need. Requests for help feel like
     an imposition rather than an opportunity for self-fulfillment. Your level
     of altruism is $flev[21].</li>
<li> <I>Cooperation</i>. Individuals who score high on this scale dislike
     confrontations. They are perfectly willing to compromise or to deny their
     own needs in order to get along with others. Those who score low on this
     scale are more likely to intimidate others to get their way. Your
     level of compliance is $flev[22].</li>
<li> <I>Modesty</i>. High scorers on this scale do not like to claim that they
     are better than other people. In some cases this attitude may derive from
     low self-confidence or self-esteem. Nonetheless, some people with high
     self-esteem find immodesty unseemly. Those who <U>are</u> willing to
     describe themselves as superior tend to be seen as disagreeably arrogant
     by other people. Your level of modesty is $flev[23].</li>
<li> <I>Sympathy</i>. People who score high on this scale are tenderhearted
     and compassionate. They feel the pain of others vicariously and are easily
     moved to pity. Low scorers are not affected strongly by human suffering.
     They pride themselves on making objective judgments based on reason.
     They are more concerned with truth and impartial justice than with mercy.
     Your level of tender-mindedness is $flev[24].</li>
</ul>
ENDOFTEXT

  print <<ENDOFTEXT;

<H2>Conscientiousness</h2>

Conscientiousness concerns the way in which we control, regulate, and direct our impulses. Impulses are not inherently bad; occasionally time constraints require a snap decision, and acting on our first impulse can be an effective response. Also, in times of play rather than work, acting spontaneously and impulsively can be fun. Impulsive individuals can be seen by others as colorful, fun-to-be-with, and zany.<P><P>

Nonetheless, acting on impulse can lead to trouble in a number of ways. Some impulses are antisocial. Uncontrolled antisocial acts not only harm other members of society, but also can result in retribution toward the perpetrator of such impulsive acts. Another problem with impulsive acts is that they often produce immediate rewards but undesirable, long-term consequences. Examples include excessive socializing that leads to being fired from one's job, hurling an insult that causes the breakup of an important relationship, or using pleasure-inducing drugs that eventually destroy one's health.<P><P>

Impulsive behavior, even when not seriously destructive, diminishes a person's effectiveness in significant ways. Acting impulsively disallows contemplating alternative courses of action, some of which would have been wiser than the impulsive choice. Impulsivity also sidetracks people during projects that require organized sequences of steps or stages. Accomplishments of an impulsive person are therefore small, scattered, and inconsistent.<P><P>

A hallmark of intelligence, what potentially separates human beings from earlier life forms, is the ability to think about future consequences before acting on an impulse. Intelligent activity involves contemplation of long-range goals, organizing and planning routes to these goals, and persisting toward one's goals in the face of short-lived impulses to the contrary. The idea that intelligence involves impulse control is nicely captured by the term prudence, an alternative label for the Conscientiousness domain. Prudent means both wise and cautious. Persons who score high on the Conscientiousness scale are, in fact, perceived by others as intelligent.<P><P>

The benefits of high conscientiousness are obvious. Conscientious individuals avoid trouble and achieve high levels of success through purposeful planning and persistence. They are also positively regarded by others as intelligent and reliable. On the negative side, they can be compulsive perfectionists and workaholics. Furthermore, extremely conscientious individuals might be regarded as stuffy and boring. Unconscientious people may be criticized for their unreliability, lack of ambition, and failure to stay within the lines, but they will experience many short-lived pleasures and they will never be called stuffy.<p><p>
<table>
<tr><td>DOMAIN/Facet</td><td>Score</td><td><img src='grphhead.jpg'></td></tr>
<tr><td>CONSCIENTIOUSNESS</td><td>$SCP</td><td><img src='bargray.jpg' width=$WCP height='20'></td></tr>
<tr><td>..Self-Efficacy</td><td>$SCFP[1]</td><td><img src='bargray.jpg' width=$WC[1] height='20'></td></tr>
<tr><td>..Orderliness</td><td>$SCFP[2]</td><td><img src='bargray.jpg' width=$WC[2] height='20'></td></tr>
<tr><td>..Dutifulness</td><td>$SCFP[3]</td><td><img src='bargray.jpg' width=$WC[3] height='20'></td></tr>
<tr><td>..Achievement-Striving</td><td>$SCFP[4]</td><td><img src='bargray.jpg' width=$WC[4] height='20'></td></tr>
<tr><td>..Self-Discipline</td><td>$SCFP[5]</td><td><img src='bargray.jpg' width=$WC[5] height='20'></td></tr>
<tr><td>..Cautiousness</td><td>$SCFP[6]</td><td><img src='bargray.jpg' width=$WC[6] height='20'></td></tr>
</table>
ENDOFTEXT

  if ($SC < $LO) {
      print <<ENDOFTEXT;
Your score on Conscientiousness is low, indicating you like to live for the moment and do what feels good now. Your work tends to be careless and disorganized. <P><P>
ENDOFTEXT
}

  if ($SC >= $LO && $SC <= $HI) {
      print <<ENDOFTEXT;
Your score on Conscientiousness is average. This means you are reasonably reliable, organized, and self-controlled. <P><P>
ENDOFTEXT
}

  if ($SC > $HI) {
      print <<ENDOFTEXT;
Your score on Conscientiousness is high. This means you set clear goals and pursue them with determination. People regard you as reliable and hard-working. <P><P>
ENDOFTEXT
}

  print <<ENDOFTEXT;

<H3>Conscientiousness Facets</h3>

<ul>
<li> <I>Self-Efficacy</i>. Self-Efficacy describes confidence in one's ability
     to accomplish things. High scorers believe they have the intelligence
     (common sense), drive, and self-control necessary for achieving success.
     Low scorers do not feel effective, and may have a sense that they are not
     in control of their lives. Your level of self-efficacy is $flev[25].</li>
<li> <I>Orderliness</i>. Persons with high scores on orderliness are
     well-organized. They like to live according to routines and schedules. They
     keep lists and make plans. Low scorers tend to be disorganized and
     scattered. Your level of orderliness is $flev[26].</li>
<li> <I>Dutifulness</i>. This scale reflects the strength of a person's sense
     of duty and obligation. Those who score high on this scale have a strong
     sense of moral obligation. Low scorers find contracts, rules, and
     regulations overly confining. They are likely to be seen as unreliable or
     even irresponsible. Your level of dutifulness is $flev[27].</li>
<li> <I>Achievement-Striving</i>. Individuals who score high on this
     scale strive hard to achieve excellence. Their drive to be recognized as
     successful keeps them on track toward their lofty goals. They often have
     a strong sense of direction in life, but extremely high scores may
     be too single-minded and obsessed with their work. Low scorers are content
     to get by with a minimal amount of work, and might be seen by others
     as lazy. Your level of achievement striving is $flev[28].</li>
<li> <I>Self-Discipline</i>. Self-discipline-what many people call
     will-power-refers to the ability to persist at difficult or unpleasant
     tasks until they are completed. People who possess high self-discipline
     are able to overcome reluctance to begin tasks and stay on track despite
     distractions. Those with low self-discipline procrastinate and show poor
     follow-through, often failing to complete tasks-even tasks they want very
     much to complete. Your level of self-discipline is $flev[29].</li>
<li> <I>Cautiousness</i>. Cautiousness describes the disposition to
     think through possibilities before acting. High scorers on the Cautiousness
     scale take their time when making decisions. Low scorers often say or do
     first thing that comes to mind without deliberating alternatives and the
     probable consequences of those alternatives. Your level
     of cautiousness is $flev[30].</li>
</ul>
ENDOFTEXT

  ($LO = 45);
  ($HI = 55);

  print <<ENDOFTEXT;

<H2>Neuroticism</h2>

Freud originally used the term <I>neurosis</I> to describe a condition marked by mental distress, emotional suffering, and an inability to cope effectively with the normal demands of life. He suggested that everyone shows some signs of neurosis, but that we differ in our degree of suffering and our specific symptoms of distress. Today neuroticism refers to the tendency to experience negative feelings. Those who score high on Neuroticism may experience primarily one specific negative feeling such as anxiety, anger, or depression, but are likely to experience several of these emotions. People high in neuroticism are emotionally reactive. They respond emotionally to events that would not affect most people, and their reactions tend to be more intense than normal. They are more likely to interpret ordinary situations as threatening, and minor frustrations as hopelessly difficult. Their negative emotional reactions tend to persist for unusually long periods of time, which means they are often in a bad mood. These problems in emotional regulation can diminish a neurotic's ability to think clearly, make decisions, and cope effectively with stress.<p><p>

At the other end of the scale, individuals who score low in neuroticism are less easily upset and are less emotionally reactive. They tend to be calm, emotionally stable, and free from persistent negative feelings. Freedom from negative feelings does not mean that low scorers experience a lot of positive feelings; frequency of positive emotions is a component of the Extraversion domain.<p><p>
<table>
<tr><td>DOMAIN/Facet</td><td>Score</td><td><img src='grphhead.jpg'></td></tr>
<tr><td>NEUROTICISM</td><td>$SNP</td><td><img src='bargray.jpg' width=$WNP height='20'></td></tr>
<tr><td>..Anxiety</td><td>$SNFP[1]</td><td><img src='bargray.jpg' width=$WN[1] height='20'></td></tr>
<tr><td>..Anger</td><td>$SNFP[2]</td><td><img src='bargray.jpg' width=$WN[2] height='20'></td></tr>
<tr><td>..Depression</td><td>$SNFP[3]</td><td><img src='bargray.jpg' width=$WN[3] height='20'></td></tr>
<tr><td>..Self-Consciousness</td><td>$SNFP[4]</td><td><img src='bargray.jpg' width=$WN[4] height='20'></td></tr>
<tr><td>..Immoderation</td><td>$SNFP[5]</td><td><img src='bargray.jpg' width=$WN[5] height='20'></td></tr>
<tr><td>..Vulnerability</td><td>$SNFP[6]</td><td><img src='bargray.jpg' width=$WN[6] height='20'></td></tr>
</table>
ENDOFTEXT

  if ($SN < $LO) {
      print <<ENDOFTEXT;
Your score on Neuroticism is low, indicating that you are exceptionally calm, composed and unflappable. You do not react with intense emotions, even to situations that most people would describe as stressful.<P><P>
ENDOFTEXT
}

  if ($SN >= $LO && $SN <= $HI) {
      print <<ENDOFTEXT;
Your score on Neuroticism is average, indicating that your level of emotional reactivity is typical of the general population. Stressful and frustrating situations are somewhat upsetting to you, but you are generally able to get over these feelings and cope with these situations.<P><P>
ENDOFTEXT
}

  if ($SN > $HI) {
      print <<ENDOFTEXT;
Your score on Neuroticism is high, indicating that you are easily upset, even by what most people consider the normal demands of living. People consider you to be sensitive and emotional.<P><P>
ENDOFTEXT
}

  print <<ENDOFTEXT;

<H3>Neuroticism Facets</h3>

<ul>
<li> <I>Anxiety</i>. The "fight-or-flight" system of the brain of anxious
     individuals is too easily and too often engaged. Therefore, people who
     are high in anxiety often feel like something dangerous is about to happen.
     They may be afraid of specific situations or be just generally fearful.
     They feel tense, jittery, and nervous. Persons low in Anxiety are generally
     calm and fearless. Your level of anxiety is $flev[1].</li>
<li> <I>Anger</i>. Persons who score high in Anger feel enraged when
     things do not go their way. They are sensitive about being treated fairly
     and feel resentful and bitter when they feel they are being cheated.
     This scale measures the tendency to <I>feel</I> angry; whether or not the
     person <I>expresses</I> annoyance and hostility depends on the individual's
     level on Agreeableness. Low scorers do not get angry often or easily.
     Your level of anger is $flev[2].</li>
<li> <I>Depression</i>. This scale measures the tendency to feel sad, dejected,
     and discouraged. High scorers lack energy and have difficult initiating
     activities. Low scorers tend to be free from these depressive feelings.
     Your level of depression is $flev[3].</li>
<li> <I>Self-Consciousness</i>. Self-conscious individuals are sensitive
     about what others think of them. Their concern about rejection and
     ridicule cause them to feel shy and uncomfortable abound others. They
     are easily embarrassed and often feel ashamed. Their fears that others
     will criticize or make fun of them are exaggerated and unrealistic, but
     their awkwardness and discomfort may make these fears a self-fulfilling
     prophecy. Low scorers, in contrast, do not suffer from the mistaken
     impression that everyone is watching and judging them. They do not feel
     nervous in social situations. Your level or self-consciousness is
     $flev[4].</li>
<li> <I>Immoderation</i>. Immoderate individuals feel strong cravings and
     urges that they have have difficulty resisting. They tend to be
     oriented toward short-term pleasures and rewards rather than long-
     term consequences. Low scorers do not experience strong, irresistible
     cravings and consequently do not find themselves tempted to overindulge.
     Your level of immoderation is $flev[5].</li>
<li> <I>Vulnerability</i>. High scorers on Vulnerability experience panic,
     confusion, and helplessness when under pressure or stress. Low scorers
     feel more poised, confident, and clear-thinking when stressed.
     Your level of vulnerability is $flev[6].</li>
</ul>
ENDOFTEXT

print <<ENDOFTEXT;

<H2>Openness to Experience</h2>

Openness to Experience describes a dimension of cognitive style that
distinguishes imaginative, creative people from down-to-earth, conventional
people. Open people are intellectually curious, appreciative of art, and
sensitive to beauty. They tend to be, compared to closed people, more aware of
their feelings. They tend to think and act in individualistic and nonconforming
ways. Intellectuals typically score high on Openness to Experience;
consequently, this factor has also been called <I>Culture</I> or
<I>Intellect</I>. Nonetheless, Intellect is probably best regarded as one aspect of openness
to experience. Scores on Openness to Experience are only modestly
related to years of education and scores on standard intelligent tests.<p><p>

Another characteristic of the open cognitive style is a facility for thinking
in symbols and abstractions far removed from concrete experience. Depending on
the individual's specific intellectual abilities, this symbolic cognition may
take the form of mathematical, logical, or geometric thinking, artistic and
metaphorical use of language, music composition or performance, or one of the
many visual or performing arts.

People with low scores on openness to experience tend to have narrow, common
interests. They prefer the plain, straightforward, and obvious over the
complex, ambiguous, and subtle. They may regard the arts and sciences with
suspicion, regarding these endeavors as abstruse or of no practical use.
Closed people prefer familiarity over novelty; they are conservative and
resistant to change.<p><p>

Openness is often presented as healthier or more mature by psychologists, who
are often themselves open to experience. However, open and closed styles of
thinking are useful in different environments. The intellectual style of the
open person may serve a professor well, but research has shown that closed
thinking is related to superior job performance in police work, sales, and
a number of service occupations.<p><p>
<table>
<tr><td>DOMAIN/Facet</td><td>Score</td><td><img src='grphhead.jpg'></td></tr>
<tr><td>OPENNESS</td><td>$SOP</td><td><img src='bargray.jpg' width=$WOP height='20'></td></tr>
<tr><td>..Imagination</td><td>$SOFP[1]</td><td><img src='bargray.jpg' width=$WO[1] height='20'></td></tr>
<tr><td>..Artistic Interests</td><td>$SOFP[2]</td><td><img src='bargray.jpg' width=$WO[2] height='20'></td></tr>
<tr><td>..Emotionality</td><td>$SOFP[3]</td><td><img src='bargray.jpg' width=$WO[3] height='20'></td></tr>
<tr><td>..Adventurousness</td><td>$SOFP[4]</td><td><img src='bargray.jpg' width=$WO[4] height='20'></td></tr>
<tr><td>..Intellect</td><td>$SOFP[5]</td><td><img src='bargray.jpg' width=$WO[5] height='20'></td></tr>
<tr><td>..Liberalism</td><td>$SOFP[6]</td><td><img src='bargray.jpg' width=$WO[6] height='20'></td></tr>
</table>
ENDOFTEXT

  if ($SO < $LO ) {
      print <<ENDOFTEXT;
Your score on Openness to Experience is low, indicating you like to think in
plain and simple terms. Others describe you as down-to-earth, practical,
and conservative.<P><P>
ENDOFTEXT
}

  if ($SO >= $LO && $SO <= $HI) {
      print <<ENDOFTEXT;
Your score on Openness to Experience is average, indicating you enjoy tradition
but are willing to try new things. Your thinking is neither simple nor
complex. To others you appear to be a well-educated person but not an intellectual.<P><P>
ENDOFTEXT
}

  if ($SO > $HI) {
      print <<ENDOFTEXT;
Your score on Openness to Experience is high, indicating you enjoy novelty,
variety, and change. You are curious, imaginative, and creative.<P><P>
ENDOFTEXT
}
  print <<ENDOFTEXT;

<H3>Openness Facets</h3>

<ul>
<li> <I>Imagination</i>. To imaginative individuals, the real world is
     often too plain and ordinary. High scorers on this scale use fantasy as a
     way of creating a richer, more interesting world. Low scorers are on this
     scale are more oriented to facts than fantasy. Your level of imagination
     is $flev[13].</li>
<li> <I>Artistic Interests</i>. High scorers on this scale love beauty, both in
     art and in nature. They become easily involved and absorbed in artistic
     and natural events. They are not necessarily artistically trained nor
     talented, although many will be. The defining features of this scale are
     <I>interest in</I>, and <I>appreciation of</I> natural and
     artificial beauty. Low scorers lack aesthetic sensitivity and interest in
     the arts. Your level of artistic interests is $flev[14].</li>
<li> <I>Emotionality</i>. Persons high on Emotionality have good access
     to and awareness of their own feelings. Low scorers are less aware of
     their feelings and tend not to express their emotions openly. Your
     level of emotionality is $flev[15].</li>
<li> <I>Adventurousness</i>. High scorers on adventurousness are eager to
     try new activities, travel to foreign lands, and experience different
     things. They find familiarity and routine boring, and will take a new
     route home just because it is different. Low scorers tend to feel
     uncomfortable with change and prefer familiar routines. Your level of
     adventurousness is $flev[16].</li>
<li> <I>Intellect</i>. Intellect and artistic interests are the two most
     important, central aspects of openness to experience. High scorers on
     Intellect love to play with ideas. They are open-minded to new and unusual
     ideas, and like to debate intellectual issues. They enjoy riddles, puzzles,
     and brain teasers. Low scorers on Intellect prefer dealing with either
     people or things rather than ideas. They regard intellectual exercises as a
     waste of time. Intellect should <U>not</u> be equated with intelligence.
     Intellect is an intellectual style, not an intellectual ability, although
     high scorers on Intellect score <U>slightly</u> higher than low-Intellect
     individuals on standardized intelligence tests. Your level of intellect
     is $flev[17].</li>
<li> <I>Liberalism</i>. Psychological liberalism refers to a readiness to
     challenge authority, convention, and traditional values. In its most
     extreme form, psychological liberalism can even represent outright
     hostility toward rules, sympathy for law-breakers, and love of ambiguity,
     chaos, and disorder. Psychological conservatives prefer the security and
     stability brought by conformity to tradition. Psychological liberalism
     and conservatism are not identical to political affiliation, but certainly
     incline individuals toward certain political parties. Your level of
     liberalism is $flev[18].</li>
</ul>
ENDOFTEXT

# Update data file
$datafile = "ipipitem.dat";
open (ITEM_FILE, ">>$datafile") || die("Cannot open data file.");
flock (ITEM_FILE, 2);
printf ITEM_FILE ("%1d%2d%2d%2d%2d%2d%2d%3d %s %s", $Gender,$Age,$sec,$min,$hour,$dom,$mon,$year,$Nick,$Country);
printf ITEM_FILE ("\n");
foreach $line1 (@line1) {
  printf ITEM_FILE ("%1d", $line1);
}
printf ITEM_FILE ("\n");
foreach $line2 (@line2) {
  printf ITEM_FILE ("%1d", $line2);
}
printf ITEM_FILE ("\n");
foreach $line3 (@line3) {
  printf ITEM_FILE ("%1d", $line3);
}
printf ITEM_FILE ("\n");
foreach $line4 (@line4) {
  printf ITEM_FILE ("%1d", $line4);
}
printf ITEM_FILE ("\n");
foreach $line5 (@line5) {
  printf ITEM_FILE ("%1d", $line5);
}
printf ITEM_FILE ("\n");
flock (ITEM_FILE, 8);
close(ITEM_FILE);

 #Close the document cleanly.
  print &HtmlBot;
}
