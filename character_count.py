s = "aab"
ans = ""
last=s[0]
count=0
for i in s:
	if i==last:
		count+=1
	else:
		ans+=str(count)+last
		count=0
		last = i
		count+=1
ans+=str(count)+last
print(ans)