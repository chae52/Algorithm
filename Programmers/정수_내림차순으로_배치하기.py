# https://programmers.co.kr/learn/courses/30/lessons/12933
def solution(n):
    s=[i for i in str(n)]
    s=sorted(s,reverse=True)
    s=int(''.join(s))
    return s
