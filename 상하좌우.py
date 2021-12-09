# https://www.youtube.com/watch?v=2zjoKjt97vQ&t=2269s

# n=5
# plan=['R','R','R','U','D','D']

now=[1,1]

for p in plan:
    if p=='R':
        if now[1]+1<n:
            now[1]+=1
    elif p=='L':
        if now[1]-1>0:
            now[1]-=1
    elif p=='U':
        if now[0]-1>0:
            now[0]-=1
    elif p=='D':
        if now[0]+1<n:
            now[0]+=1
print(now)
