T=int(input())
a, b, c=300, 60, 10
A=T//a
T=T%a
B=T//b
T=T%b
C=T//c
T=T%c
if T!=0:
    print(-1)
else:
    print(A,B,C)
