import sys
n,l=map(int,sys.stdin.readline().split(' '))

pond=list()
for i in range(n):
    start,end=map(int,sys.stdin.readline().split(' '))
    pond.append((start,end))

pond.sort()
cnt=0
now=pond[0][0]

for start,end in pond:
    if now<start:
        now=start
    while now >=start and now<end:
        now+=l
        cnt+=1
print(cnt)
