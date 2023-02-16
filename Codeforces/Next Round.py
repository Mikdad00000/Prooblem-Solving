koijon, rno = map(int,input().split())
arr=list(map(int,input().split()))
arr.sort(reverse= True)
mark= arr[rno-1]
counter = 0
for x in arr:
    if mark <= x and x > 0:
        counter=counter + 1
print(counter)

