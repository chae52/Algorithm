n,m=map(int, input().split(' '))
day=list()
for i in range(n):
    day.append(int(input()))
start=max(day)
end=start*n
answer=start

def is_possible(current,count,mid):
    for money in day:
        if current >= money:  #돈이 모자르지 않음
            current-=money
        else: # 돈이 모자름
            count+=1
            current=mid # 남은 돈 다 넣고 인출
            current-=money
        
    return count

while start<= end:
    mid=(start+end)//2

    cnt=is_possible(0,0,mid)
    if cnt <= m:
        answer=mid
        end=mid-1
    # elif cnt<m:
    #     end=mid-1
    elif cnt>m:
        start=mid+1
    
print(answer)
