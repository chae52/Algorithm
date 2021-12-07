# https://programmers.co.kr/learn/courses/30/lessons/12930 
def solution(s):
    answer = ''
    s=s.split(' ')
    for ss in s:
        for i,sss in enumerate(ss):
            if i%2==0: #짝수
                answer+=ss[i].upper()
            else:
                answer+=ss[i].lower()
        answer+=' '
    return answer[:-1]
