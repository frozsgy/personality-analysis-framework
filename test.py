# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"^RT @[A-Za-z0-9_]{1,}: (.*?)$"

test_str = ("RT @frozsgy: hello from the other side\n"
    "tesla\n"
    "RT @BirGun_Gazetesi: AKP'li isimden, Sivas Katliamı'na 'Sivas Katliamı' diyenler hakkında suç duyurusu: \"\"Sivas'ın imajını zedeliyorlar\"\"\n"
    "htt…")

test_tuple = ("RT @frozsgy: hello from the other side"
    ,"tesla"
    ,"RT @BirGun_Gazetesi: AKP'li isimden, Sivas Katliamı'na 'Sivas Katliamı' diyenler hakkında suç duyurusu: \"\"Sivas'ın imajını zedeliyorlar\"\"\n htt…")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    #print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    if len(match.groups()) > 0:
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            
            print(match.group(groupNum))
            #print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
    else :
        print("hery")

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.

print("-"*80)

for i in test_tuple:
    date_search = re.search(regex, i, flags=re.S)
    if date_search:
        date_match = re.search(regex, i, flags=re.S)
        dates = date_match.groups()
        print(dates[0])
    else :
        print(i)