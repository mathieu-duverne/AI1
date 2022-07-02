

def main():
    
    li = fiveInt()
    
    croissant = recursive(li)
    print('')
    print("list depart")
    print(li)
    print("liste croissant")
    print(croissant)
    print('')
    
    
def fiveInt():
    li = []
    i = 0
    while True:
        
        if i < 5:
            number = int(input("enter your input : "))
            li.append(number)
            i +=1
            
        else:
            break
        
    return li


def recursive(li):

    for y in range(len(li)):
        
        temp = 0
        if y + 1 == 5:
            break
        
        if li[y + 1] < li[y]:
            
            temp = li[y]
            li[y] = li[y + 1]
            li[y + 1] = temp
            recursive(li)    
                    
    return li



if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    