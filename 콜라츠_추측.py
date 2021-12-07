# https://programmers.co.kr/learn/courses/30/lessons/12943
def solution(num):
    for i in range(500):
        if num==1:
            break
        if num%2==0:
            num//=2
        else:
            num=num*3+1
    if i==499:
        answer=-1
    else:
        answer=i
    return answer
