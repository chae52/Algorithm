# https://www.youtube.com/watch?v=7C9RgOcvkvo&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=3
# n=4
# m=5
# ice=[[0,0,1,1,0],[0,0,0,1,1],[1,1,1,1,1],[0,0,0,0,0]]
# ice=[[1,1,1,0,1],[1,0,1,0,1],[0,0,0,0,1],[1,1,1,1,1]]
# ice=[[0,0,0,1,0],[0,1,0,1,0],[1,1,1,1,0,],[0,0,0,0,0]]

def freeze(x,y):
    if x>=n or x<=-1 or y>=m or y<=-1:
        return False
    if ice[x][y]==0:
        ice[x][y] = 1
        freeze(x,y+1)
        freeze(x,y-1)
        freeze(x+1,y)
        freeze(x-1,y)
        return True
    return False #ice[x][y] 가 1일 때

answer=0
for i in range(0,n):
    for j in range(0,m):
        if freeze(i,j) ==True:
            answer+=1
print(answer)
