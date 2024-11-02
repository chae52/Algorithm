import sys
from collections import deque
input=sys.stdin.readline
n,m= map(int, input().split(' '))
graph=[]
wall=[]
di = [[1,0,-1,0],[0,1,0,-1]]     # 남동북서 = 1 1 1 1
times=[0]
for i in range(m):
    graph.append(list(map(int, input().split(' '))))
    walls=[]
    for x in graph[i]:
        walls.append('{0:0>4}'.format(bin(x)[2:]))
    wall.append(walls)
def bfs(x,y, visited, num):
    if not visited[x][y]:
        q=deque([])
        t=1
        q.append([x,y])
        visited[x][y]=num

        while q:
            x,y = q.popleft()
            # print('{0:04d}'.format(int(bin(graph[x][y])[2:])))
            for i in range(4):
                dx,dy= x+di[0][i], y+di[1][i]
                if wall[x][y][i]=='0' and not visited[dx][dy]:
                    t+=1
                    q.append([dx,dy])
                    visited[dx][dy]=num
        times.append(t)
        return t,visited
    return 0,visited
                    
answer1=0
visited=[[False]*n for _ in range(m)]
num=1

for i in range(m):
    for j in range(n):
        time,visited=bfs(i,j,visited, num)
        if time >0:
            answer1+=1
            num+=1
print(answer1)
print(max(times))

answer3=0
for i in range(m):
    for j in range(n):
        for k in range(4):
            xi,xj = i+di[0][k], j+di[1][k]
            if 0<=xi<m and 0<=xj<n and visited[xi][xj]!=visited[i][j]:
                answer3=max(answer3,times[visited[xi][xj]]+times[visited[i][j]] )
print(answer3)