# https://programmers.co.kr/learn/courses/30/lessons/12977
from itertools import combinations
def solution(nums):
    answer = 0
    data = combinations(nums, 3)
    for i in data:
        if prime(sum(i)) == True:
            answer+=1
    return answer

def prime(num):
    for i in range(2,num):
        if num%i ==0:
            return False
    return True
        
