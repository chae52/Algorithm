import sys
n=int(sys.stdin.readline())
k=int(sys.stdin.readline())
sensor = list(map(int, sys.stdin.readline().split(' ')))
sensor = sorted(list(sensor))

if n <= k:
    print(0)
    exit()

length = []
for i in range(len(sensor) - 1):
    length.append(sensor[i + 1] - sensor[i])
length.sort()
result=0
for i in range(k-1):
    length.remove(max(length))

print(sum(length))
