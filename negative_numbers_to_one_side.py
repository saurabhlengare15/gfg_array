arr = [1 ,-1 ,-3 , -2, 7, 5, 11, 6]
n = len(arr)
j = 0
for i in range(0, n) :
    if arr[i]>0 :
        arr[i],arr[j] = arr[j],arr[i]
        j+=1
print(arr)