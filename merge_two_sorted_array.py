arr1 = [1,2,3,4,5]
arr2 = [1,2,3,5,89,100,102]
op = []
first=0
second=0
while(first<len(arr1) and second<len(arr2)):
    if(arr1[first]<=arr2[second]):
        op.append(arr1[first])
        first+=1

    else:
        op.append(arr2[second])
        second+=1

while(first<len(arr1)):
    op.append(arr1[first])
    first+=1

while(second<len(arr2)):
    op.append(arr2[second])
    second+=1

print(op)