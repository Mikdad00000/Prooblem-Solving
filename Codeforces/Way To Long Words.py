a = input()
b = int(a)
while b > 0:
    c = input()
    if len(c) < 11:
        print(c)   
    else:
        f = len(c)
        g = c[0] 
        h = c[-1]
        j = f - 2
        print(g + str(j) + h)
    b = b - 1

