import sys
n=int(sys.stdin.readline())
# 00 11
# 000 001 100
# 0000 1001 0011 1100 1111
# 00000 10000 00001 11001 00111 10011 11100 11111
# 000000 100100 001001 100001 100111 111001 001100 000011 110000 111100 001111 110011 111111
a,b=1,1
if n==1:
    print(1)
else:
    for _,i in enumerate(range(n-1)):
        c=a+b
        c%= 15746
        a=b
        b=c
    print(c)