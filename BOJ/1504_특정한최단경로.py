import sys
from collections import defaultdict
import heapq
input=sys.stdin.readline
n,e=map(int,input().split(' '))
graph=defaultdict(list)

for _ in range(e):
    a,b,cost=map(int,input().split(' '))
    graph[a].append([b,cost])
    graph[b].append([a,cost])
one,two=map(int,input().split(' '))
INF=1e9
def dijkstra(start):
    distance=[INF]*(n+1)
    q=[]
    heapq.heapify(q)
    heapq.heappush(q,(start,0))
    distance[start]=0
    
    while q:
        now,dist=heapq.heappop(q)
        if distance[now]<dist:
            continue
        
        for next in graph[now]:
            cost=next[1]+dist
            if cost<distance[next[0]]:
                distance[next[0]]=cost
                heapq.heappush(q,(next[0], cost))
    return distance
      
one_dist=dijkstra(1) # 1-> one
two_dist=dijkstra(one) #one->two
end_dist=dijkstra(two) # two->n

one2two=one_dist[one]+two_dist[two]+end_dist[n]
two2one=one_dist[two]+end_dist[one]+two_dist[n]
answer= one2two if one2two<two2one else two2one
if answer>=INF:
    answer=-1
print(answer)
