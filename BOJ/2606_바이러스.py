import sys

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

graph = dict()
for i in range(n):
    graph[i + 1] = []
for i in range(m):
    a,b=map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
result = 0

def dfs(v, visited):
    global result
    if visited[v]==True:
        return
    visited[v] = True

    for i in graph[v]:
        if visited[i]==False:
            result += 1
            dfs(i, visited)

dfs(1, visited)
print(result)
