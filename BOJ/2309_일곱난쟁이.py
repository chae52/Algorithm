from collections import deque
import itertools

n=list()
for i in range(9):
    n.append(int(input()))
out=list(itertools.combinations(n,2))

s=sum(n)

for i,j in out:
    if s-i-j==100:
        n.remove(i)
        n.remove(j)
        break

n.sort()
for i in n:
    print(i)
