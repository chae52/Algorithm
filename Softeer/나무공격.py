import sys
input=sys.stdin.readline

n,m = map(int, input().strip().split(' '))
graph=[list(map(int, input().strip().split(' '))) for i in range(n)]
a,b = map(int, input().strip().split(' '))
c,d = map(int, input().strip().split(' '))

answer=[0]*n
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            answer[i]+=1
for i in range(a, b+1):
    if answer[i-1]>0:
        answer[i-1]-=1
for i in range(c, d+1):
    if answer[i-1]>0:
        answer[i-1]-=1
print(sum(answer))