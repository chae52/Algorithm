# https://programmers.co.kr/learn/courses/30/lessons/76501
def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i]==False:
            absolutes[i]*=-1
        answer=answer+ absolutes[i]
    return answer
