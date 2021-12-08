# https://www.youtube.com/watch?v=2zjoKjt97vQ&t=1s

# n=5
# ad=[2,3,1,2,2]

ad.sort()

answer=0
temp=1
for a in ad:
    if temp>=a:
        answer+=1
        temp=1
    else:
        temp+=1
        
print(answer)
