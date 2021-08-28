strr = "abcbcbc"
strr = list(strr)
for i in range(len(strr)):
    for j in range(0,len(strr)-i-1):
        if strr[j]>strr[j+1]:
            strr[j],strr[j+1] = strr[j+1],strr[j]

for i in strr:
    print(i,end="")