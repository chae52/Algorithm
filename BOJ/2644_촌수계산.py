from collections import defaultdict
from sys import setrecursionlimit
setrecursionlimit(10**6)
n=int(input()) # 전체 사람 수

a,b =map(int,input().split(' ')) # 촌수를 구해야 하는 두 사람
m=int(input()) # 관계 수

graph=defaultdict(list)
for i in range(m):
    x,y= map(int,input().split(' '))# x: 부모, y: 자식
    graph[x].append(y)
    graph[y].append(x)
# print('graph',graph)

def dfs(a,chon,visited):
    childs=graph[a]
    chon+=1
    visited.append(a)
    if b in childs: # 도착
        print(chon)
        exit()
    else:
        for child in childs:
            if child not in visited:
                dfs(child,chon,visited)

visited=[]
dfs(a,0,visited)
print(-1)
