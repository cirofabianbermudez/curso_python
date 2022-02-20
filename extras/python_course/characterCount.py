##import pprint
##
##message = 'This is a test string, to count how many letters are'
##count = {}
##
##for character in message.upper():
##    count.setdefault(character, 0)
##    count[character] = count[character] + 1
##
##text = pprint.pformat(count)
##print(text)
##    
##    

import pprint

message = 'This is a test string, to count how many letters are'
count = {}

for character in message:
    count.setdefault(character,0)
    count[character] += 1

##text = pprint.pformat(count)
##print(text)
pprint.pprint(count)
