import sys
input=sys.stdin.readline

n=int(input())
times=list()

for i in range(n):
    times.append(list(map(int, input().split(' '))))
times.sort()
if n==1:
    print(times[0][2])
else:
    dp_table=[0]*n
    dp_table[0]=times[0][2]
    dp_table[1]=max(dp_table[0],times[1][2])
    for i in range(2,n):
        dp_table[i]=max(dp_table[i-1],dp_table[i-2]+times[i][2])
    print(dp_table[-1]) 