# top down : 시간초과

import sys
sys.setrecursionlimit(10**6)
n=int(input())

def makeOne(n):
    # 종료조건
    if n==1:
        return 0

    # 메모이제이션
    if d[n]!=0:
        return d[n]
    
    # 재귀 호출
    d[n]=makeOne(n-1)+1
    if n%3==0:
        d[n]=min(d[n], makeOne(n//3)+1)

    elif n%2==0:
        d[n]=min(d[n], makeOne(n//2)+1)

    return d[n]
d=[0]*(n+1)
print(makeOne(n))

# bottom up
n=int(input())
d=[0]*(n+1)
d[1]=0

for i in range(2,n+1):
    # print("**********",i)
    d[i]=d[i-1]+1
    # print(f"-1 d[i] = {d[i]}")
    if i%3==0:
        d[i]=min(d[i], d[i//3]+1)
        # print(f"%3 d[i] = {d[i]}")

    if i%2==0:
        d[i]=min(d[i], d[i//2]+1)
print(d[n])
