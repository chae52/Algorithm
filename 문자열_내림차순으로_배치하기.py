def solution(s):
    ords=[ord(ss) for ss in s]
    answer=''
    while ords:
        max_st=max(ords)
        answer+=chr(max_st)
        ords.remove(max_st)
    return answer
