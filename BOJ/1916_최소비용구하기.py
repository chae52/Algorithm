from collections import defaultdict
import heapq
n=int(input())
m=int(input())
graph=defaultdict(list)
for _ in range(m):
    start, end, cost=map(int, input().split(' '))
    graph[start].append((cost, end))

start_city,end_city=map(int, input().split(' '))

distance=[int(1e9)]*(n+1)
def dijkstra(start_city):
    q=[]
    heapq.heappush(q, (0, start_city))
    distance[start_city]=0

    while q:
        dist, now=heapq.heappop(q)
        
        if distance[now]<dist:
            continue

        for i in graph[now]:
            cost=dist+i[0]

            if cost<distance[i[1]]:
                distance[i[1]]=cost
                heapq.heappush(q, (cost,i[1]))

dijkstra(start_city)
print(distance[end_city])
