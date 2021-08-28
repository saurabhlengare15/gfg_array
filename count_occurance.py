arr = [3,1,2,2,1,2,3,3]
n = 8
k = 4
dict = {}
count = 0
for i in arr:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
                
for i in dict:
    if dict[i] > n/k:
        count+=1
                
print(count)