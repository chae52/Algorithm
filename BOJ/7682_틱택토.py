import sys
input=sys.stdin.readline
x=input().strip()

case=[[0,3,6],
      [1,4,7],
      [2,5,8],
      [0,1,2],
      [3,4,5],
      [6,7,8],
      [0,4,8],
      [2,4,6]]

while x != 'end':
    x_count, o_count=0,0
    x_win, o_win=False, False
    answer='invalid'
    for i in x:
        if i=='X':
            x_count+=1
        elif i=='O':
            o_count+=1     
    if x_count==o_count+1 or x_count == o_count:#정상 갯수
        for i in range(len(case)):
            if x[case[i][0]]!='.' and x[case[i][0]]==x[case[i][1]] and x[case[i][1]]==x[case[i][2]]: # 누군가 이김
                winner=x[case[i][0]]
                if winner=='X':
                    x_win=True
                elif winner == 'O':
                    o_win=True
                    
        if x_count==o_count+1: # x가 놓음
            if not o_win and x_win: # O가 이겼는데 X가 또 놓을 수 없음
                answer='valid'

                
            if x_count==5 and not o_win:
                answer='valid'

        else: # o가 놓음
            if not x_win and o_win:
                answer='valid'
            elif not x_win and not o_win: # 더 놓을 수 있는 상태라 종료상태가 아님
                answer='invalid'
            else:
                answer='invalid'

    else: # 비정상 갯수
        answer='invalid'
        
    x=input().strip()
    print(answer)