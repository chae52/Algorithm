from collections import deque
r,c=map(int,input().split(' '))
graph=list()
for _ in range(r):
    graph.append(input())

visited=[[False]*c for _ in range(r)]

dx=[1,-1,0,0]
dy=[0,0,1,-1]
result_k,result_v=0,0

for i in range(r):
    for j in range(c):
        k,v, = 0,0
        q=deque([(i,j)])
        while q:
            now_i,now_j= q.popleft()
            if visited[now_i][now_j]==True:
                continue
            if graph[now_i][now_j]=='#':
                continue
            
            visited[now_i][now_j]=True
            
            if graph[now_i][now_j]=='k':
                k+=1
            elif graph[now_i][now_j] == 'v':
                v+=1
            for d in range(len(dx)):
                x=dx[d]+now_i
                y=dy[d]+now_j
                if x<r and x>=0 and y<c and y>=0:
                    if graph[x][y]!='#' or graph[x][y]==False:
                        q.append((x,y))
           
        if k-v>0:
            result_k+=k
        else:
            result_v+=v

print(result_k,result_v)
