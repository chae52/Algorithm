import sys
input=sys.stdin.readline

n=int(input())
answer=list()
for i in range(n):
    l=input().strip().split('.')
    if len(l)==2:
        answer.append([int(l[0]),int(l[1])])
    else:
        answer.append([int(l[0]),-1])

answer=sorted(answer,key =lambda x : (x[0], x[1]))

for i in range(n):
    s=''
    s+=str(answer[i][0])
    if answer[i][1]!=-1:
        s+='.'
        s+=str(answer[i][1])
    print(s)