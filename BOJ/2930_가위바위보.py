import sys

r=int(sys.stdin.readline())
sg=sys.stdin.readline().strip()
n=int(sys.stdin.readline())
play=['' for _ in range(n)]
for i in range(n):
    play[i]=sys.stdin.readline().strip()
result=0 

result_dict=dict(RR=1,SS=1,PP=1, RS=2,PR=2,SP=2, SR=0,RP=0,PS=0)
max_rsp=[[[0,0,0] for _ in range(n)]for x in range(r)] 

for i,s in enumerate(play): 
    for j,c in enumerate(s):
        result += result_dict[sg[j]+c]
        max_rsp[j][i][0] += result_dict['R' + c]
        max_rsp[j][i][1] += result_dict['S' + c]
        max_rsp[j][i][2] += result_dict['P' + c]
max_result=0 
for i in range(r):
    round_max = [0, 0, 0]
    for j in range(n):
        for t in range(3):
            round_max[t]+=max_rsp[i][j][t]
    max_result+=max(round_max)

print(result)
print(max_result)
