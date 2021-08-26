arr = [1,2,3,4,5,6,7,8,9,10]
s = 15
for i in range(len(arr)):
    sum = arr[i]
    for j in range(i+1,len(arr)):
        sum = sum+arr[j]
        
        if sum == s:
            print(i,j)
