import matplotlib.pyplot as plt
import numpy as np

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

dict = {}
for letter in listOfWord:
    
    if len(letter) in dict:
        dict[len(letter)] += 1
        
    else:
        dict.update({len(letter): 1})

keys = []
keys = sorted(dict.keys())
values = dict.values()
plt.bar(keys, values, tick_label=keys)
plt.show()