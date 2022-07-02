def stringInput():
    string = str(input("give me a string without uppercase and freespace : "))
    str1 = string.replace(" ", "")
    str2 = str1.lower()
    return str2

def main(string, countRecursion, o, p):
    temp = ""
    nbrLetter = len(string)
    li = list(string.strip())
    # print(o,p)
    # print()
    # ---- Permutation avant derniere et derniere
    if li[nbrLetter - p] < li[nbrLetter - o]:
        temp = li[nbrLetter - p]
        li[nbrLetter - p] = li[nbrLetter - o]
        li[nbrLetter - o] = temp
        listToStr = ''.join([str(elem) for elem in li])
        print("chaine de caractere apres")
        print(listToStr)
    
    else:
        o += 1
        p += 1
        listToStr = ''.join([str(elem) for elem in li])
        countRecursion += 1
        main(listToStr, countRecursion, o, p)
        

    

    

if __name__ == "__main__":
    
    beautifulString = stringInput()
    print("chaine de caractere avant")
    print(beautifulString)
    result = main(beautifulString, countRecursion=0, o=1, p=2)
    
    