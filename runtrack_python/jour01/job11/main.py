def add(x, y):
    return x + y
x = 1
y = 2
while True:
    if x < 5:
        result = add(x, y)
        x += 1
        y += 1 
        print(result)
    else:
        break