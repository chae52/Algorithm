import sys
input=sys.stdin.readline
n=int(input())

def sortStudents(students):
    students=students[1:]
    move=0
    sorted_students=[students[0]]
    
    for i in range(1, len(students)):
        flag=False
        for j in range(len(sorted_students)):
            if sorted_students[j]>students[i]:
                move+=(len(sorted_students)-j)
                sorted_students=sorted_students[:j]+[students[i]]+sorted_students[j:]
                flag=True
                break
    
        if flag==False: # 본인 보다 큰 사람이 한 명도 없음
            sorted_students.append(students[i])
    return move
    
for i in range(n):
    t=list(map(int,input().split(' ')))
    print(i+1, sortStudents(t))