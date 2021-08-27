arr1 = [1,2,3,4,5,8,35]
arr2 = [1,2,3,4,7,8,30,34,56]
op = []
first=0
second=0
while(first<len(arr1) and second<len(arr2)):
    if(arr1[first]<=arr2[second]):
        op.append(arr1[first])
        op.append(arr2[second])

    else:
        op.append(arr2[second])
        op.append(arr1[first])

    first+=1
    second+=1

if(first<len(arr1)):
    op.append(arr1[first])
    first+=1

if(second<len(arr2)):
    op.append(arr2[second])
    second+=1

print(op)