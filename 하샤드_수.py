# https://programmers.co.kr/learn/courses/30/lessons/12947
def solution(x):
    h=0
    xx=x
    while xx>0:
        h+=xx%10
        xx=xx//10
    return x%h==0
