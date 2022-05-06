n=int(input())
a=list(map(int,input().split(' ')))
a.sort()
m=int(input())
check=list(map(int,input().split(' ')))

def check_exist(check,a):
    start=0
    end=len(a)
    exist=0
    while start<=end:
    
        mid=(start+end)//2
        if mid>=n:
            break

        if a[mid]==check:
            exist=1
            break
        elif a[mid]>check:
            end=mid-1
        elif a[mid]<check:
            start=mid+1
    print(exist)

for i in check:
    check_exist(i,a)
