# https://programmers.co.kr/learn/courses/30/lessons/42748 
def solution(array, commands):
    answer = []
    for c in commands:
        sub=sorted(array[c[0]-1:c[1]])
        answer.append(sub[c[2]-1])
    return answer
