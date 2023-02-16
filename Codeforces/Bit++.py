counter = 0
b = int(input())
while (b > 0):
    x = input()
    if (x[1] == "+"):
        counter = counter + 1
    else:
        counter = counter - 1
    b = b - 1
print(counter)
