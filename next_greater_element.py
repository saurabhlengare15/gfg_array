arr = [1,3,2,4]
for i in range(0,len(arr)):
    next = -1
    for j in range(i+1,len(arr)):
        if arr[i]<arr[j]:
            next = arr[j]
            break
    print(next)