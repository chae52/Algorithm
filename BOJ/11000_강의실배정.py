import sys
import heapq

n=int(sys.stdin.readline())
time=list()
for i in range(n):
    s,t = map(int, sys.stdin.readline().split(' '))
    time.append((s,t))

time.sort()
room=[0]

for s,t in time:
    if room[0] <= s:
        heapq.heappop(room)
    heapq.heappush(room, t)

print(len(room))
