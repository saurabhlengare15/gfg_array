arr = [0,1,0,0,2,1,2,2]
c0=0
c1=0
c2=0
for i in range(len(arr)):
    if arr[i] == 0:
        c0+=1
    if arr[i] == 1:
        c1+=1
    if arr[2] == 2:
        c2+=1

for i in range(c0):
    arr[i] = 0
for i in range(c0,c0+c1):
    arr[i] = 1
for i in range(c0+c1,len(arr)):
    arr[i] = 2

print(arr)

    