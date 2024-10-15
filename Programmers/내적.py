# https://programmers.co.kr/learn/courses/30/lessons/70128
def solution(a, b):
    return sum([c*d for c,d in zip(a,b)])
