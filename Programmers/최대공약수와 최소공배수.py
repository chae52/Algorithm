# https://programmers.co.kr/learn/courses/30/lessons/12940

# 라이브러리 사용
import math
def solution(n, m):
    return [math.gcd(n,m),int(n*m/math.gcd(n,m))]

#라이브러리 미사용
def solution(n, m):
    for i in range(1,m+1):
        if n%i==0 and m%i==0:
            a=i
    return [a,int(n*m/a)]
