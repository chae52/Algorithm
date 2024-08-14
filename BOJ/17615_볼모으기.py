n=int(input())
balls=input()

def move(balls):
    even=0
    odd=0
    cnt=1
    now_ball=balls[0]
    is_even=True
    balls=balls[1:]
    for i,ball in enumerate(balls):
        if ball == now_ball:
            cnt+=1
        else:
            now_ball=ball
            if is_even:
                even+=cnt
                is_even=False
            else:
                odd+=cnt
                is_even=True
            cnt=1
    return even, odd
a,b=move(balls)
c,d=move(balls[::-1])
print(min(a,b,c,d))