n=int(input())
loss=list(map(int,input().split(' ')))
loss.sort()

answer=0
if n%2==1:
    answer=max(answer, loss[-1])
    s=2
else:
    s=1
for i in range((n-1)//2):
    now=loss[i]+loss[-(i+s)]
    answer=max(answer,now)

print(answer)
