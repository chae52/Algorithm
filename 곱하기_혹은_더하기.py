# https://www.youtube.com/watch?v=2zjoKjt97vQ&t=1s

# s='02984'
# s='567'
answer=0
for i,ss in enumerate(s):
    ss=int(ss)
    if i==0:
        answer=ss
    else:
        if answer>0:
            answer*=ss
        else:
            answer+=ss
print(answer)
