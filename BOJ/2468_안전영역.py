import sys
sys.setrecursionlimit(10000)
def dfs(x, y, water,graph,visited):
    if x < 0 or x >= n or y >= n or y < 0:
        return False
    if visited[y][x]==True:
        return False

    if graph[y][x] > water:
        visited[y][x] = True
        dfs(x + 1, y, water,graph,visited)
        dfs(x - 1, y, water,graph,visited)
        dfs(x, y + 1, water,graph,visited)
        dfs(x, y - 1, water,graph,visited)
        return True
    else:
        return False

n = int(sys.stdin.readline().strip())
graph=[]
for i in range(n):
    graph_inner = list(map(int, sys.stdin.readline().strip().split()))
    graph.append(graph_inner)

highest=max(max(graph))
result = 1
for water in range(1,highest):
    visited=[[False]*n for _ in range(n)]
    water_result=0
    for x in range(n):
        for y in range(n):
            if dfs(x, y, water,graph,visited) == True:
                water_result += 1
    if result <= water_result:
        result=water_result
print(result)
