arr = [6,1,15,19,9,13,12,6,7,2,10,4,1,14,11,14,14,13]
peak = arr[0]
for i in arr:
    if i>peak:
        peak=i
print(peak)