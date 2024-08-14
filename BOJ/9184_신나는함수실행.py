import sys
input= sys.stdin.readline
seq=list()
a,b,c = list(map(int, input().split(' ')))
seq.append([a,b,c])
while (not(a==-1 and b==-1 and c==-1)):
    a,b,c = list(map(int, input().split(' ')))
    seq.append([a,b,c])

dp_table=[[[0]*21 for _ in range(21)] for _ in range(21)]
dp_table[0][0][0]=1
    
def w(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return dp_table[0][0][0]
    if a>20 or b>20 or c>20:
        return w(20,20,20)
    if a<b and b<c:
        if dp_table[a][b][c]==0:
            dp_table[a][b][c]=w(a,b,c-1) + w(a,b-1,c-1) -w(a,b-1,c)
        return dp_table[a][b][c]
    else:
        if dp_table[a][b][c]==0:
            dp_table[a][b][c]=w(a-1,b,c)+w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dp_table[a][b][c]

for i in range(len(seq)-1):
    a,b,c=seq[i]
    answer=w(a,b,c)
    s='w('+str(a)+', '+str(b)+', '+str(c)+') = '+str(answer)
    print(s)