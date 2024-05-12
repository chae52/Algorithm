import sys
input = sys.stdin.readline
n,m= map(int,input().split(' '))
nums=list(map(int,input().split(' ')))

prefix_sum=[0]*n
prefix_sum[0]=nums[0]
for i in range(1,n):
    prefix_sum[i]=prefix_sum[i-1]+nums[i]

for i in range(m):
    s,e = map(int,input().split(' '))
    if s-2<0:
        print(prefix_sum[e-1])
    else:
        print(prefix_sum[e-1]-prefix_sum[s-2])