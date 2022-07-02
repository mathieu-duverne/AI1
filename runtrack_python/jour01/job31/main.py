def main(li):
    
    newLi = []
    for i in li:
        if (i + 1) % 5 == 0:
            newLi.append(i + 1)
            
        elif (i + 2) % 5 == 0:
            newLi.append(i + 2)
            
        else:
            newLi.append(i)
            
    return newLi

        

if __name__ == "__main__":
    
    li = [82, 12, 83 , 90, 95, 100]
    print("note avant arrondissement")
    print(li)
    result = main(li)
    print('note arrondie')
    print(result)   
              