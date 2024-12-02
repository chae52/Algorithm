import sys
input=sys.stdin.readline
n=int(input())
first,second,third,fourth=list(),list(),list(),list()
i=0
for a,b,c in zip(list(map(int,input().strip().split(' '))),list(map(int,input().strip().split(' '))),list(map(int,input().strip().split(' ')))):
    first.append([a,i])
    second.append([b,i])
    third.append([c,i])
    fourth.append([a+b+c, i])
    i+=1
def cal(scores):
    scores.sort(reverse=True)
    result=[0]*n
    rank=1
    result[scores[0][1]]=1
    wait=1
    for i in range(1,n):
        if scores[i-1][0] == scores[i][0]:
            wait+=1  
        else:
            rank+=wait
            wait=1
        result[scores[i][1]]=rank
    return result

print(*cal(first))
print(*cal(second))
print(*cal(third))
print(*cal(fourth))
