from collections import defaultdict
import heapq
INF=1e9
n,p,k=map(int,input().split(' '))
graph=defaultdict(list)

for i in range(n):
    graph[i+1]

for _ in range(p):
    a,b,cost=map(int,input().split())
    graph[a].append((b,cost))
    graph[b].append((a,cost))

print(graph)

distance=[INF]*(n+1)
distance[0]=None
parents={i : 0 for i in graph}
def dijkstra(start):
    q=[]
    heapq.heappush(q, (0,start)) # 첫 cost=0
    distance[start]=0

    while q:
        dist, now=heapq.heappop(q)

        if distance[now]<dist:
            continue

        for node in graph[now]:
            next_node,next_dist=node[0],node[1]
            cost=dist+next_dist

            if cost<distance[next_node]:
                distance[next_node]=cost
                parents[next_node]=now
                heapq.heappush(q,(cost,next_node))
        


dijkstra(1)
print('parents',parents)
print(distance[n])
