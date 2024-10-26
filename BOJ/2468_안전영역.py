import sys
from collections import deque
sys.setrecursionlimit(10000)
di=[[1,0,-1,0],[0,1,0,-1]]
def bfs(x, y, water,graph,visited):
    if x < 0 or x >= n or y >= n or y < 0 or visited[x][y]==True:
        return False,visited
    q=deque([[x,y]])
    answer=0
    while q:
        x,y=q.popleft()
        if 0<=x and x<n and 0<=y and y<n and visited[x][y] ==False and graph[x][y] > water:
            visited[x][y] = True
            answer+=1
            for i in range(4):
                dx,dy = x+di[0][i], y+di[1][i]
                q.append([dx,dy])

    if answer>0:
        return True, visited
    else:
        return False, visited
input=sys.stdin.readline
n = int(input())
graph=[]
for i in range(n):
    graph.append(list(map(int, input().strip().split())))

result = 1
for water in range(1,101):
    visited=[[False]*n for _ in range(n)]
    water_result=0
    for x in range(n):
        for y in range(n):
            yn, visited=bfs(x, y, water,graph,visited)

            if  yn == True:
                water_result += 1

    if result <= water_result:
        result=water_result
print(result)