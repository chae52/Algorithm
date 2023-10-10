import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
board=[[0]*n for _ in range(n)]
k=int(input())
for _ in range(k):
    x,y=list(map(int,input().split(' ')))
    board[x-1][y-1]=2

l=int(input())
turn=dict()
for _ in range(l):
    x,c=input().strip().split(' ')
    x=int(x)
    turn[x]=c

time=0
d='R'
di={'R':[0,1],'L':[0,-1],'U':[-1,0],'D':[1,0]}
head=[0,0]
board[0][0]=1
snake=deque([[0,0]])

# 오른쪽으로 'R'->'D'->'L'->'U'
right_turn={'R':'D','D':'L','L':'U','U':'R'}
# 왼쪽으로  'L'->'D'->'R'->'U'
left_turn={'L':'D','D':'R','R':'U','U':'L'}

while True:
    # 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
    head[0]+=di[d][0]
    head[1]+=di[d][1]
    time+=1
    # 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
    if head[0]>=n or head[0]<0 or head[1]>=n or head[1]<0:
        break
    if board[head[0]][head[1]]==1:
        break
    
    # 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
    if board[head[0]][head[1]]==2:
        snake.append([head[0],head[1]])
        board[head[0]][head[1]]=1
        # snake.append(head)
    # 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
    if board[head[0]][head[1]]==0:
        snake.append([head[0],head[1]])
        board[head[0]][head[1]]=1
        x,y=snake.popleft()
        board[x][y]=0
    
    if time in turn.keys():
        if turn[time]=='D':
            d=right_turn[d]
        else:
            d=left_turn[d]
    
print(time)