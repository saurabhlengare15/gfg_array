arr = [7,10,4,3,20,15]
k=3
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            arr[i],arr[j] = arr[j],arr[i]

print(arr[k-1])