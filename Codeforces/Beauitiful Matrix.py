r1 = list(map(int, input().split()))
r2 = list(map(int, input().split()))
r3 = list(map(int, input().split()))
r4 = list(map(int, input().split()))
r5 = list(map(int, input().split()))
f = [r1, r2, r3, r4, r5]
r = 0
c   = 0 
p = []
while r < 5:
    while c < 5:
        if f[r][c] == 1:
            p = [r, c]
        c = c + 1
    c = 0 
    r = r + 1
x = abs(2 - p[0])
y = abs(2 - p[1])
print(x + y)




# [(0,0), (0,1), (0, 2), (0, 3), (0, 4)]
# [(1,0), (1,1), (1, 2), (1, 3), (1, 4)]
# [(2,0), (2,1), (2, 2), (2, 3), (2, 4)]
# [(3,0), (3,1), (3, 2), (3, 3), (3, 4)]
# [(4,0), (4,1), (4, 2), (4, 3), (4, 4)]
