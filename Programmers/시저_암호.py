# https://programmers.co.kr/learn/courses/30/lessons/12926
def solution(s, n):
    answer = ''
    for i,ss in enumerate(s):
        if ss==' ':
            answer+=' '
        else:
            if (97<=ord(ss)<=122 and ord(ss)+n>122) or(65<=ord(ss)<=90 and ord(ss)+n>90):
                answer+=chr( ord(ss)+n -26)
            else:
                answer+=chr( ord(ss)+n )
    return answer
