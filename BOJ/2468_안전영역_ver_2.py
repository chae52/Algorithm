import sys
sys.setrecursionlimit(10000)
def dfs(x, y, water,graph,visited):
    if x < 0 or x >= n or y >= n or y < 0:
        return False,visited
    if visited[x][y]==True:
        return False,visited

    if graph[x][y] > water:
        visited[x][y] = True
        _, visited = dfs(x + 1, y, water,graph,visited)
        _, visited = dfs(x - 1, y, water,graph,visited)
        _, visited = dfs(x, y + 1, water,graph,visited)
        _, visited = dfs(x, y - 1, water,graph,visited)
        return True,visited
    else:
        return False,visited

n = int(sys.stdin.readline().strip())
graph=[]
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip().split())))

result = 1
for water in range(1,101):
    visited=[[False]*n for _ in range(n)]
    water_result=0
    for x in range(n):
        for y in range(n):
            yn, visited=dfs(x, y, water,graph,visited)
            if  yn == True:
                water_result += 1
    if result <= water_result:
        result=water_result
print(result)