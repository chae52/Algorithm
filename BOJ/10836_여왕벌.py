import sys
input=sys.stdin.readline
m,n= map(int, input().split(' '))
plus=[1]+[0]*(m-1)*2
last=[0]*(2*m-1)
for i in range(n):
    seq=list(map(int, input().split(' ')))
    now=0
    for j in range(3):
        now+=seq[j]

        if j!=2:
            if now>2*m-2:
                continue
            else:
                plus[now]+=1
            
now=0
for i in range(0,len(plus)):
    now+=plus[i]
    last[i]=now
    
for idx, i in enumerate(range(0,m)):
    print(last[idx+m-1], end=' ')
print('')
for i in range(m-2,-1,-1):
    print(last[i], end=' ')
    for idx, i in enumerate(range(1,m)):
        print(last[idx+m], end=' ')
    print('')