n=int(input())
if n==0:
    print(0)
    exit()
seq=range(0,n)

start=0
end=n
while start<=end:
    mid=(start+end)//2

    if mid**2 >= n and (mid-1)**2<n:
        print(mid)
        exit()
    elif mid**2<n:
        start=mid+1
        continue
    elif (mid+1)**2 >= n :
        end=mid-1
