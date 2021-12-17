# https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    runner={}
    for i in participant:
        runner[i]=0
    for i in participant:
        runner[i]+=1
    for i in completion:
        if i in runner:
            runner[i]-=1
    for i in runner:
        if runner[i]==1:
            return i
