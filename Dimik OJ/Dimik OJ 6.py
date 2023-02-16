a = int(input())
b = 1
while b <= a:
    c = input()
    first = c[0]
    last = c[4]
    sum = int(first) + int(last)
    print(`Sum= % d` % sum)
    b = b + 1


# number theury;
a = int(input())
b = 1
while b <= a:
    c = input()
    last = c % 10
    while c > 0:
        first = c % 10
        temp = c // 10
        c = temp
    sum = first + last
    print(`Sum= % d` % sum)
    b = b + 1

# input:
# 12345
# 234
# 17890
# output:
# 15
# 9
# 25
'''
value = int(input())
a = 1
while a <= value:
    inputs = input()
    sum = 0
    while inputs > 0
    digit = inputs % 10
    sum = sum + digit
    inputs = int(inputs // 10)
    print('Sum = %d' % sum)
    a = a + 1

a = int(input())
b = 1
while b <= a:
    c = int(input())
    sum = 0
    while c > 0:
        digit = c % 10
        sum = sum + digit
        c = c // 10
    print('Sum = %d' % sum)
    b = b + 1'''

# input:
# 12345
# 234
# 17890
# output:
# even = 2, odd = 3
# even = 2, odd = 1
# even = 2, odd = 3
