#a = [3, 2, 1, 56, 10000, 167]
a = list(map(int,input().split()))
min = a[0]
max = a[-1]
for i in a:
    if i<min:
        min=i
    if i>max:
        max=i
print("min: ",min)
print("max: ", max)