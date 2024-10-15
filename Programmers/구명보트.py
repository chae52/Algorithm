# https://programmers.co.kr/learn/courses/30/lessons/42885
def solution(people, limit):
    answer = 0
    people.sort()
    biggest=len(people)-1
    smallest=0
    rescued=[]
    boat=0
    while len(rescued) != len(people):
        if smallest>=biggest:
            break
        if people[smallest]+people[biggest]<=limit:
            rescued.append(people[smallest])
            rescued.append(people[biggest])
            boat+=1
            smallest+=1
            biggest-=1
        else:
            biggest-=1
        # print(rescued,smallest,biggest)
    boat+=len(people)-len(rescued)
    return boat
