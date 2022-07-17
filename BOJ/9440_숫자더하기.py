import math
def nextnum(i,nums):
    if i==0: # 첫 번째 수는 0 이면 안 됨
        next=nums[-1]
        if next==0:
            # 0이 아니면서 가장 작은 수를 가져옴
            num_copy=nums.copy()
            while num_copy[-1] == 0:
                # print('0 is coming')
                num_copy.pop()

            # 원래 리스트에서 해당 수를 지움
            next=num_copy.pop()
            nums.remove(next)
            return next
        else:
            return nums.pop()

    else:
        return nums.pop()

x=input()
while int(x.split(' ')[0]) != 0:
    n=int(x.split(' ')[0])
    nums = list(map(int,x.split(' ')))[1:]
    
    nums.sort(reverse=True)
    num1=''
    num2=''

    for i in range(0,n,2):
        num1=num1+str(nextnum(i,nums))
        if n/2 !=0 and i==n-1:
            continue
        num2=num2+str(nextnum(i,nums))
        
    print(int(num1)+int(num2))
    x=input()
