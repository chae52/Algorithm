n=int(input())

seq=list(map(int,input().split(' ')))
d=[1]*(n)

for i in range(n):
    for j in range(i):
        if seq[i]>seq[j]:
            d[i]=max(d[i],d[j]+1) # d[i-1]+1
            
print(max(d))
