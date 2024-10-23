from itertools import product

t=int(input())
def eval_cal(formula: str):
    answer=0
    formula='+'+formula
    idx=len(formula)-1
    prev=0
    while idx>=0:
        if formula[idx] =='+':
            prev=int(formula[idx+1:])
            answer+=prev
            formula=formula[:idx]
        elif formula[idx] =='-':
            prev=int(formula[idx+1:])
            answer-=prev
            formula=formula[:idx]
        idx-=1
    return answer
        
for i in range(t):
    n=int(input())
    answer=list()
    iters_print=[['+', '-', ' '] for _ in range(n-1)]
    iters_cal=[['+', '-', ''] for _ in range(n-1)]

    candidates_print=list(product(*iters_print))
    candidates_cal=list(product(*iters_cal))

    for can_print, can_cal in zip(candidates_print,candidates_cal):
        ex=''
        for j in range(0,n-1):
            ex+=str(j+1)
            ex+=can_cal[j]
        ex+=str(n)

        if eval_cal(ex)==0:
            ex=''
            for j in range(0,n-1):
                ex+=str(j+1)
                ex+=can_print[j]
            ex+=str(n)
            answer.append(ex)
    answer.sort()
    for ans in answer:
        print(ans)
    print('')