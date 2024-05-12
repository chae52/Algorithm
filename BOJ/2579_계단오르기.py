n=int(input())
stairs=list()
for _ in range(n):
    stairs.append(int(input()))

dp=[0]*n
if n==1:
    print(stairs[0])
    exit()
dp[0]=stairs[0]
if n==2:
    print(stairs[0]+stairs[1])
    exit()
dp[1]=stairs[0]+stairs[1]
if n==3:
    print(max(dp[0]+stairs[2], stairs[1]+stairs[2]))
    exit()
dp[2]=max(dp[0]+stairs[2], stairs[1]+stairs[2])

for i in range(3,n):
    dp[i]=max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i])
print(dp[n-1])
