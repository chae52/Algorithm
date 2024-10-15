from itertools import combinations
def solution(numbers):
    data = list(combinations(numbers, 2))
    answer=list(set([d[0]+d[1] for d in data]))
    answer.sort()
    return answer
