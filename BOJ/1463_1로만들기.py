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
