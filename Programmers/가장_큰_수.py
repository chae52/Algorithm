# https://programmers.co.kr/learn/courses/30/lessons/42746

# 시간초과
import itertools
def solution(numbers):
    data=list( itertools.permutations(numbers,len(numbers)))
    new=[]
    for n in data:
        x= [i for i in n]
        x=''.join([str(j) for j in x])
        new.append(x)
    return max(new)
