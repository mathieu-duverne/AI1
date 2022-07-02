import re

p = '.'
v = ','
pp = ':'
pv = ';'
pi = '?'
pe = '!'

f = open("jour03/job02/data.txt", "r")
stringData = f.read()
newString = ''
for l in stringData:
    
    if l == p or l == v or l == pp or l == pv or l == pi or l == pe:
        pass
    else:
        newString += l
        
listOfWord = []
word = ''
for le in newString:
    if le == " ":
        listOfWord.append(word)
        word = ''
        
    if le != " ":
        word += le
        
listOfWordOk = []
for m in listOfWord:
    if m.isalnum(): 
        listOfWordOk.append(m)

print(len(listOfWordOk))