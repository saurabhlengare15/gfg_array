arr = [1,2,3,5]
n = 5
sum = ((n+1)*n)//2
real_sum = 0
for i in arr:
    real_sum += i
print(sum-real_sum)