import matplotlib.pyplot as plt
import numpy as np

p = '.'
v = ','
pp = ':'
pv = ';'
pi = '?'
pe = '!'
d = '-'
s= '\n'
e = '*'
z = '+'

f = open("jour03/job02/data.txt", "r")
stringData = f.read().lower()

newString = ''
for l in stringData:
    
    if l == p or l == v or l == pp or l == pv or l == pi or l == pe or l == d or l == s or l == e or l == z:
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
        
        
# print(listOfWord)
dict = {}
for word in listOfWord:
    if not len(word):
        continue
    
    elif word[0] in dict:
        dict[word[0]] += 1
        
    else:
        dict.update({word[0]: 1})
# print(dict)
keys = []
keys = sorted(dict.keys())
values = dict.values()
plt.bar(keys, values, tick_label=keys)
plt.show()