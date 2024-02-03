import sys
from collections import deque
input=sys.stdin.readline

m,n = map(int,input().strip().split(' '))
graph=list()
for i in range(n):
    graph.append(list(map(int,input().strip().split(' '))))

ripe=list()
normal_tomato=n*m
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            ripe.append([i,j,0])
            normal_tomato-=1
        elif graph[i][j]==-1:
            normal_tomato-=1

def bfs(ripe, graph, normal_tomato):
    q=deque(ripe)
    di=[[1,0,-1,0],[0,1,0,-1]]
    day=0
    while q:
        x,y,day=q.popleft()
        
        for i in range(4):
            dx=x+di[0][i]
            dy=y+di[1][i]
            
            if 0<=dx and dx<n and 0<=dy and dy<m and graph[dx][dy]==0:
                graph[dx][dy]=1
                normal_tomato-=1
                q.append([dx,dy,day+1])
    return day, normal_tomato

bfs_day, nt=bfs(ripe, graph, normal_tomato)

if nt>0:
    print(-1)
else:
    print(bfs_day)