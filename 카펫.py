#https://programmers.co.kr/learn/courses/30/lessons/42842#
import math
def solution(brown, yellow):
    answer = []
    total=brown+yellow
    sqrt=math.sqrt(total)
    int_sqrt=int(sqrt)
    if sqrt==(int_sqrt):
        return [int_sqrt,int_sqrt]
    for i in range(int_sqrt+1, 0,-1):
        x=total/i
        if x ==int(x):
            answer=[i,total/i]
            answer.sort(reverse=True)
            if (answer[0]-2)*(i-2)==yellow:
                break
    answer.sort(reverse=True)  
        
    return answer
