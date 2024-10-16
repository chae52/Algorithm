n=int(input())
time=[0]*(n+1)
buildings=[[]]

for i in range(n):
    l=list(map(int, input().split(' ')))
    time[i+1]=l[0]
    buildings.append(l[1:-1])
result_time=[0]*(n+1)

def dfs(b):
    if result_time[b]!=0:
        return result_time[b]
    max_time=0
    for i in range(len(buildings[b])):
        if result_time[buildings[b][i]]==0:
            result_time[buildings[b][i]]=dfs(buildings[b][i])
        max_time=max(max_time, result_time[buildings[b][i]])
    result_time[b]=max_time+time[b]
    return result_time[b]
            
for i in range(1,n+1):
    result_time[i]=dfs(i)
    print(result_time[i])