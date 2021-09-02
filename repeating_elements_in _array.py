arr = [3,2,1,3,4,5,2,6]
visited = set()
dup = set()
for i in arr:
    if i in visited:
        dup.add(i)
    visited.add(i)
    
print(dup)