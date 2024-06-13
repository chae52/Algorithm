import sys
from collections import defaultdict
import heapq
input=sys.stdin.readline
n,d=map(int, input().split(' '))
graph= defaultdict(list)
for i in range(0,d):
    graph[i].append([i+1,1])
for i in range(n):
    s,e,cost=map(int, input().split(' '))
    graph[s].append([e,cost])
dist=[1e9]*(d+1)

def dijkstra(node,dist):
    heap=[[0,0]]
    heapq.heapify(heap)
    dist[node]=0
    while heap:
        cost,node = heapq.heappop(heap)
        if node==d:
            break
        if dist[node]<cost:
            continue
        if node in graph.keys():
            for e, c in graph[node]:
                if e>d:
                    continue
                next_cost = c + cost

                if next_cost<dist[e]:
                    dist[e]=next_cost
                    heapq.heappush(heap,[next_cost, e])
    return dist
                
dist = dijkstra(0,dist)
print(dist[d])
