s = "words"
s1 = "sword"

s = list(s)
s1 = list(s1)

for i in range(len(s)):
	for j in range(i+1,len(s)):
		if ord(s[i])>ord(s[j]):
			s[i],s[j] = s[j],s[i]

for i in range(len(s1)):
	for j in range(i+1,len(s1)):
		if ord(s1[i])>ord(s1[j]):
			s1[i],s1[j] = s1[j],s1[i]

if s==s1:
	print("anagram")
else:
	print("not anagram")