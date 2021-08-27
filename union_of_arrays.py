a = [85,25,1,32,54,6]
b = [85,2]
for i in b:
    if i in a:
        a.remove(i)
                
op = b+a
print(list(set(op)))
print(len(op))