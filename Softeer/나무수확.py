import sys
from itertools import product
input=sys.stdin.readline

n=int(input())
graph=list()
dp=[[[0,0] for _ in range(n)] for _ in range(n)]

for i in range(n):
    graph.append(list(map(int, input().strip().split(' '))))
for i in range(n):
    for j in range(n):
        dp[i][j]=[0,0] # [스프링쿨러 사용, 스프링쿨러 미사용]
dp[0][0]=[graph[0][0],graph[0][0]*2]

for i in range(1,n):
    dp[0][i][0]=dp[0][i-1][0]+graph[0][i]
    dp[i][0][0]=dp[i-1][0][0]+graph[i][0]

    dp[0][i][1]=dp[0][i-1][0]+graph[0][i]*2
    dp[i][0][1]=dp[i-1][0][0]+graph[i][0]*2

for i in range(1,n):
    for j in range(1,n):
        dp[i][j][0]=max(dp[i-1][j][0]+graph[i][j], dp[i][j-1][0]+graph[i][j])
        
        dp[i][j][1]=max(dp[i][j][0] + graph[i][j], # 이번에 스프링쿨러 사용
                       dp[i-1][j][1] + graph[i][j],
                       dp[i][j-1][1] + graph[i][j])

print(dp[n-1][n-1][1])