# https://www.youtube.com/watch?v=2zjoKjt97vQ&t=2269s
# n=5

answer=0
def sec_to_hms(now):
    s=now%60
    now=now//60
    m=now%60
    h=now//60
    return h,m,s

for now in range(1,(n+1)*60*60):
    h,m,s=sec_to_hms((now))
    if '3' in str(h) or '3' in str(m) or '3' in str(s):
        answer+=1

print(answer)


