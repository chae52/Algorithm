import sys
input=sys.stdin.readline

n=int(input().strip())
graph=list()
for i in range(n):
    graph.append(list(map(int,input().strip().split(' '))))

blue=0
white=0
direction=[[0,0,1,1],[0,1,0,1]]

def check(n,x,y):
    color=graph[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if graph[i][j]!=color:
                return False
    return True

def s(n,x,y):
    global blue
    global white
    if n==1:
        if graph[x][y]:
            blue+=1
        else:
            white+=1
    else:
        if check(n,x,y):
            if graph[x][y]:
                blue+=1
            else:
                white+=1
            return
        next_n=n//2
        for i in range(4):
            s(next_n,x+direction[0][i]*next_n,y+direction[1][i]*next_n)
s(n,0,0)

print(white)
print(blue)