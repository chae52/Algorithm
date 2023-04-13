n=int(input())
notes=input()
new_notes=notes[0]
now=notes[0]
for i in range(1,len(notes)):
    if now!=notes[i]:
        new_notes+=notes[i]
        now=notes[i]

answer=len(new_notes)
cnt=1
if len(new_notes)<3:
    new_answer=len(new_notes)
else:
    while len(new_notes)>=3: # 반복문 하지 않고 수학적으로 개선 가능성 있음
        new_notes=new_notes[2:]
        new_answer=len(new_notes)+cnt
        cnt+=1
print(min(new_answer,answer))
