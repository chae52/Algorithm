n=int(input()) #len(city)
distance=list(map(int,input().split(' ')))
city=list(map(int,input().split(' ')))
now=0 # city index
next=1
answer=0
while now<n-1:
    if city[now]<= city[next]:
        next+=1
    else:
        for i in range(now,next):
            answer+=distance[i]*city[now]
        now=next
        next+=1
    
    if next>=n-1: # city 1 2
        for i in range(now,next):
            answer+=distance[i]*city[now]
        break
    
    if now>=n-1:
        break
if now==0:
    answer=city[now]*sum(distance)
print(answer)