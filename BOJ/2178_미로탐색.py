import sys
from collections import deque
input=sys.stdin.readline

n,m = list(map(int, input().split(' ')))

graph=[] 

for i in range(n):
    graph.append(input().strip())

di = [[1,0,-1,0],[0,1,0,-1]]
def bfs(x,y):
    q=deque([(x,y,1)])
    visited = [[False]*m for _ in range(n)]
    while q:
        x,y,time = q.popleft()
        
        if x==n-1 and y==m-1:
            return time
        
        for i in range(4):
            dx, dy = x+di[0][i], y+di[1][i]
            
            if 0<=dx<n and 0<=dy<m and graph[dx][dy] == '1' and visited[dx][dy] == False:
                visited[dx][dy] = True
                q.append((dx, dy, time+1))
                
print(bfs(0,0))