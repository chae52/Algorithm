import sys
n=int(input())
c=list()
for i in range(n):
    c.append(int(input()))
result=[[] for i in range(n)]
for i in range(n):
    result[i].append(c[i]//25)
    c[i]=c[i]%25
    result[i].append(c[i] // 10)
    c[i] = c[i] % 10
    result[i].append(c[i] // 5)
    c[i] = c[i] % 5
    result[i].append(c[i])

s=''
for i in range(len(result)):
    for j in range(4):
        s=s+str(result[i][j])+' '
    print(s[:-1])
    s=''
