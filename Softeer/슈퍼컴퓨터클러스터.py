import sys
from collections import defaultdict
input=sys.stdin.readline

n,m=map(int, input().strip().split(' '))
computers=list(map(int, input().strip().split(' ')))
computers.sort()
com_dict=defaultdict(int)
for com in computers:
    com_dict[com]+=1

lo=computers[0]
hi=10**16
answer=lo

def is_possible(mid):
    coms=list(com_dict.keys())
    coms.sort()
    cost=0
    for com in coms:
        if com<=mid:
            cost+=com_dict[com]*((mid-com)**2)
        else:
            break
            
    if cost<=m:
        return True
    else:
        return False

while lo<=hi:
    mid=(lo+hi)//2

    if is_possible(mid):
        lo=mid+1
        answer=mid
    else:
        hi=mid-1

print(answer)