# https://www.youtube.com/watch?v=KGyK-pNvWos&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=4

# n,k=5,3

# a=[1,2,5,4,3]
# b=[5,5,6,6,5]

for i in range(k):
    a[a.index(min(a))], b[b.index(max(b))]=b[b.index(max(b))],a[a.index(min(a))]
    
#n**2의 시간이라 별로이다.
print(sum(a))
