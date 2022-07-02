import matplotlib.pyplot as plt
import numpy as np

f = open("jour03/job02/data.txt", "r")
stringData = f.read()

dict = {}
for letter in stringData.lower():
    if letter in dict:
        dict[letter] += 1
        
    else:
        dict.update({letter: 1})

keys = dict.keys()
values = dict.values()
plt.bar(keys, values)
plt.show()