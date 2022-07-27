t=int(input())
n=list()
for i in range(t):
    n.append(int(input()))
# print(n)
d=[0]*12
def dp(n):
    # 종료조건
    if n==1 : return 1
    if n==2 : return 2
    if n==3 : return 4

    # 메모이제이션
    if d[n]!=0:
        return d[n]

    # 재귀 호출
    d[n]=dp(n-1)+dp(n-2)+dp(n-3)
    return d[n]
    
for x in n:
    print(dp(x))
