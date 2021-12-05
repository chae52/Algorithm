# https://programmers.co.kr/learn/courses/30/lessons/86051
def solution(numbers):    
    num=set(range(0,10))
    sub=num-set(numbers)
    return sum(sub)
