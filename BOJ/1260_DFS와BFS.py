from collections import deque,defaultdict
n,m,v=map(int,input().split(' '))
graph=defaultdict(list)

nodes=list()
for mm in range(m):
    first, second=map(int,input().split(' '))
    graph[first].append(second)
    graph[second].append(first)
    nodes.append(first)

for node in nodes:
    graph[node].sort()

def dfs(v, graph, visited,dfs_answer):
    visited[v]=True # 방문 처리
    dfs_answer=dfs_answer+str(v)+' '
    print(v,end=' ')
    for g in graph[v]:
        # print('g',g)
        if visited[g]==False:
            visited[g]==True
            dfs(g,graph,visited,dfs_answer)

def bfs(v, graph, visited,bfs_answer):
    q=deque([v])

    while q:
        now=q.popleft()
        if visited[now]==False:
            visited[now]=True
            print(now, end=' ')
            
            bfs_answer=bfs_answer+str(now)+' '
            for s in graph[now]:
                q.append(s)

visited=[False]*(n+1) # 0 번째 사용 안함
dfs_answer=''
dfs(v,graph,visited,dfs_answer)
print(dfs_answer)

bfs_answer=''
visited=[False]*(n+1) # 0 번째 사용 안함
bfs(v,graph,visited,bfs_answer)
print(dfs_answer)
