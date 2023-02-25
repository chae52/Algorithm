from collections import deque
import heapq
answer=[]
heapq.heapify(answer)
m,n,k=map(int,input().split(' '))
box=list()
for i in range(k):
   box.append(list(map(int,input().split(' '))))
   #y1, x1, y2, x2
graph=[[False]*n for _ in range(m)]
# print(graph)
for b in box:
   y1, x1, y2, x2=b
   for i in range(x1,x2):
      for j in range(y1,y2):
            graph[i][j]=True
# print(graph) # 문제의 그래프와 상하대칭
di=[[0,1,0,-1],[1,0,-1,0]]
def bfs(x,y):
   q=deque([[x,y]])
   graph[x][y]=True
   cnt=1
   while q:
      x,y=q.popleft()
      
      for i in range(4):
         dx,dy=x+di[0][i], y+di[1][i]
         if 0<=dx<m and 0<=dy<n and graph[dx][dy]==False:
            graph[dx][dy]=True
            cnt+=1
            q.append([dx,dy])
            
   return cnt
for i in range(m):
   for j in range(n):
      if graph[i][j]==False:
         heapq.heappush(answer,bfs(i,j))
print(len(answer))
for i in range(len(answer)):
    print(heapq.heappop(answer),end=' ')
