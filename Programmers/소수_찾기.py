# https://programmers.co.kr/learn/courses/30/lessons/42839
import itertools
def solution(numbers):
    answer = 0
    numbers=[int(n) for n in numbers]
    new=[]
    for i in range(1,len(numbers)+1):
        temp=[list(j) for j in itertools.permutations(numbers,i)]
        for t in temp:
            new.append(''.join(str(x) for x in t))    
    new=set(map(int,new))

    if 1 in new:
        new.remove(1)
    if 0 in new:
        new.remove(0)
    
    for n in new:
        flag=0
        for j in range(2,n):
            if n%j==0:
                flag=1
                break
        if flag==0:
            answer+=1
    return answer
