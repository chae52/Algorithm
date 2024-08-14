n=int(input())
rf=0
df=0
def recursive_fib(n):
    global rf
    if n==1 or n==2:
        rf+=1
        return 1
    else:
        return recursive_fib(n-1)+recursive_fib(n-2)

dp_table=[0]*(n+1)

def dynamic_fib(n):
    global df
    dp_table[1],dp_table[2]=1,1
    
    for i in range(3,n+1):
        dp_table[i]=dp_table[i-1]+dp_table[i-2]
        df+=1
    return dp_table[n]

recursive_fib(n)
dynamic_fib(n)

print(rf,df)