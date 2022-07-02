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

# print(len(listOfWord))
dict = {}
for word in listOfWord:
    
    for i in range(len(word)):

        # -----
        # si mot exist dand dict et qu'il existe dans sou dict increment sinon init a 1 
        # si mot n'existe pas initialize
        # -----
        
        if not len(word):
            continue
        
        if (i+1) <= len(word):
            break
        
        elif word[i] in dict:
            if word[i + 1] in dict[word[i]]:
                dict[word[i]] += 1
            else:
                dict[word[i]] = word[i + 1]
                dict[word[i]][word[i + 1]] = 1 
        else:
            dict.update({word[i] : {word[i + 1] : 1 }})
            
print(dict)