import re


text = input()
print("input: " + text)

# removing the hashtag sign
text = text.replace("#", "")
print("removed hashtags: " + text)

# removing the RT keyword that gets added automatically when a RT'd tweet is fetched via the API
text = text.replace("RT", "")
print("removed RT's: " + text)

# removing mentions

# username details: https://help.twitter.com/en/managing-your-account/twitter-username-rules
# username limit: 15 chars
# [A-Za-z], [0-9], [_]
# regex for mentions => @[A-Za-z0-9_]{1,15}

# this is a bit tricky because if we remove everything starting with @, we might remove non-valid usernames as well.

# regex = r"^@[A-Za-z0-9_]{1,15}$"
"""
text2 = text.split()
for i in text2:
    matches = re.finditer(regex, i, re.MULTILINE)


    for matchNum, match in enumerate(matches, start=1):
        
        print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
        
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            
            print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
"""

# removing mentions without the username length restriction
regex = r"@[A-Za-z0-9_]{1,}"
text = re.sub(regex, '', text)
print("removed mentions: " + text)

# TODO -- BUGGY
# twitter uses t.co for url's so we can use a regex to match that only if the api gets stuff with t.co 
# for example https://t.co/BLABLA
# removing URL's 
#regex = r"(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-z]{2,8}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)"
regex = r"(http(s)?:\/\/t.co\/)[a-zA-Z0-9]+"
text = re.sub(regex, '', text)

print("removed URL's: " + text)
# remove stopwords
# -- TODO -- 



# remove extra whitespace
# method 1: regex --> leaves extra whitespace at the beginning or the end, might need trim
#regex = r"\s+"
#text = re.sub(regex, ' ', text)

# method 2: 
text = ' '.join(text.split())

print("removed whitespace: " + text)