import sys
sys.setrecursionlimit(10000)
def dfs(x, y, graph):
    if x < 0 or x >= m or y >= n or y < 0:
        return False

    if graph[y][x] == 1:
        graph[y][x] = 0
        dfs(x + 1, y, graph)
        dfs(x - 1, y, graph)
        dfs(x, y + 1, graph)
        dfs(x, y - 1, graph)
        return True
    else:
        return False


t = int(sys.stdin.readline().strip())
for tt in range(t):
    m, n, k = map(int, sys.stdin.readline().strip().split())

    graph = [[0] * m for _ in range(n)]
    for kk in range(k):
        x, y = map(int, sys.stdin.readline().strip().split())
        graph[y][x] = 1

    result = 0
    for y in range(n):
        for x in range(m):
            if dfs(x, y, graph):
                result += 1
    print(result)
