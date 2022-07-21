nums=list(map(int,input().split(' ')))
cnt=11

for i in range(nums[0],nums[1]+1):
    if '8' in str(i):
        temp_cnt=str(i).count('8')

        if temp_cnt<cnt:
            cnt=temp_cnt
    else:
        cnt=0
        break
print(cnt)
