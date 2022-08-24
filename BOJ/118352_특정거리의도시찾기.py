from collections import defaultdict
import heapq
INF=1e9
n,m,k,x=map(int,input().split(' '))
graph=defaultdict(list)

for i in range(n):
    graph[i+1]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)

distance=[INF]*(n+1)
distance[x]=0
# 다익스트라
q=[]
heapq.heappush(q, (0,x))

while q:
    dist, now=heapq.heappop(q)

    if distance[now]<dist:
        continue
    for i in graph[now]: # 인접노드 i
        cost=dist+1
        if cost<distance[i]:
            distance[i]=cost
            heapq.heappush(q, (cost, i))

cnt=0
for i in range(1,len(distance)):
    if distance[i]==k:
        print(i)
        cnt+=1
if cnt==0:
    print(-1)
