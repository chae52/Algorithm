# 틀림 주의

# 조합 : 시간초과
# from itertools import combinations
# for tc in range(3):
#     n=int(input())
#     coins=[]
#     for i in range(n):
#         coin,k=map(int,input().split(' '))
#         coins.extend([coin]*k)
#     sum_coins=sum(coins)
#     flag=False    
#     for i in range(1, len(coins)//2+1):
#         candidates=list(combinations(coins,i))
#         for can in candidates:
#             if sum_coins//2==sum(can):
#                 flag=True
#                 break
#         if flag:
#             break
#     print(int(flag))
# def find2mini(price,coins):
    
# DP : 18%
def dp(price,coins):
    
    if price in coins.keys() and coins[price]>0:
        return True
    
    else:
        all_coins=sorted(coins.keys(),reverse=True)
        flag=False
        for i in range(len(all_coins)):
            if price>all_coins[i] and coins[all_coins[i]]>0:
                flag=True
                break
        if flag==False:
            return False
        coins[all_coins[i]]-=1
        # print('all_coins[i],price-all_coins[i]',all_coins[i],price-all_coins[i])
        return dp(all_coins[i],coins)*dp(price-all_coins[i],coins)
    
for tc in range(3):
    n=int(input())
    coins=dict()
    sum_coins=0
    for i in range(n):
        coin,k=map(int,input().split(' '))
        coins[coin]=k
        sum_coins+=coin*k
    
    print(int(dp(sum_coins//2,coins)))
