n=int(input())
k=int(input())
cards=[int(input()) for _ in range(n)]
answer=set()
candidates=[]
def back(cards,k,comb,visited):
    if len(comb)==k:
        candidates.append(comb[:])
        return
    
    for i in range(n):
        if not visited[i]:
            comb.append(str(cards[i]))
            visited[i]=True
            back(cards,k,comb,visited)
            comb.pop()
            visited[i]=False
visited=[False]*n
back(cards,k,[],visited)

for can in candidates:
    answer.add("".join(can))
    
print(len(answer))
