import sys
from collections import deque
sys.setrecursionlimit(10**6)

n, m= map(int,input().split(' '))
graph=[]
for mm in range(m):
    graph.append(list(map(int, input().split(' '))))

full_count=0 # 총 0의 갯수 = 익어야하는 토마토 갯수
ripe=deque()
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0 :
            full_count+=1
        if graph[i][j]==1:
            ripe.append([i,j])

x=[1,0,-1,0]
y=[0,-1,0,1]

def bfs(graph,ripe,days,count):
    while True :
        next_ripe=deque() # per day
        while ripe:
            now = ripe.popleft()
            i=now[0]
            j=now[1]
            for direction in range(len(x)):
                if i+y[direction] >=0 and i+y[direction]< m and j+x[direction] >=0 and j+x[direction]<n:
                    if graph[i+y[direction]][j+x[direction]] ==0:
                        graph[i+y[direction]][j+x[direction]]=1
                        count+=1
                        next_ripe.append([i+y[direction], j+x[direction]])

        if not next_ripe:
            break
        days +=1
        ripe=next_ripe
    return days,count

days, count = bfs(graph,ripe,0,0)

if full_count == count:
    print(days)
else : 
    print(-1)
