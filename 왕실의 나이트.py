# https://www.youtube.com/watch?v=2zjoKjt97vQ&t=2269s
# location='a1'
# location='c2'

now=[int(location[1]), ord(location[0])-96]
answer=0
x=[-2,-2,-1,1,2,2,1,-1]
y=[-1,1, 2,2, 1,-1,-2,-2]

for dx,dy in zip(x,y):
    if 0<now[0]+dx<9 and 0<now[1]+dy<9:
        answer+=1

print(answer)


