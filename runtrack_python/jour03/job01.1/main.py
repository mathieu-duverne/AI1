f = open("jour03/job01.1/domains.xml", "r")

cont = f.read()
listAdresse = []
for i in range(len(cont)):
    adresse = ''
    if "d" == cont[i] and "o" == cont[i + 1] and "m" == cont[i + 2] and "a" == cont[i + 3] and "i" == cont[i + 4] and "n" == cont[i + 5] and ">" == cont[i + 7]:
        adresse += cont[i + 8]
        # print(adresse)
        for y in range(30):
            if cont[i + 8 + y] != "<":
                adresse += cont[i + 8 + y]
            else:
                listAdresse.append(adresse)
                break 
            
allExt = []
for x in range(len(listAdresse)):
    ext = ''
    for l in reversed(listAdresse[x]):
        if l != '.':
            ext += l
        else:
            allExt.append(ext[::-1])
            break

# print(allExt)
differentExt = []
for g in allExt:
    if g in differentExt:
        pass
    else:
        differentExt.append(g)
        result = allExt.count(g)
        print(result, g)

