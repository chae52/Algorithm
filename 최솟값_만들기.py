# https://programmers.co.kr/learn/courses/30/lessons/12941 
def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    return sum([i*j for i,j in zip(A,B)])
