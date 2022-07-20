n= int(input())
signal=input()
one_line=n//5
x=list()

def check_num(x,i):
    if i ==one_line-1:
        return 1,1
    if x[0][i+1]==0 and x[2][i+1]==0:
        return 1,1

    num_list=list()
    for j in range(0,5):
        num_list.append(x[j][i:i+3])

    if num_list[2][1]==0: #0,7
        if num_list[1][0]==0:
            result=7
        else:
            result=0
    else: # 2,3,4,5,6,8,9
        if num_list[0][1]==0:
            result=4
        else: # 2,3,5,6,8,9
            if num_list[1][0]==0 and num_list[1][1]==0: # 2,3
                if num_list[3][0]==0:
                    result=3
                else:
                    result=2
            else: # 5,6,8,9
                if num_list[1][2]==0: # 5,6
                    if num_list[3][0]==1:
                        result=6
                    else:
                        result=5
                else: #8,9
                    if num_list[3][0]==1:
                        result=8
                    else:
                        result=9

    return 3,result

for i in range(0,5):
    this_line=signal[one_line*i:one_line*(i+1)]
    splited=list()
    for char in this_line:
        if char== '#':
            splited.append(1)
        else:
            splited.append(0)
    x.append(splited)

patience=0
last_result=''
for i in range(0,one_line):
    if x[0][i]==1 and patience==0 :
        patience,result=check_num(x,i)
        last_result+=str(result)
    if patience>0:
        patience-=1

print(last_result)
