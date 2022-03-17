import sys
formula=sys.stdin.readline().strip()
plus_split_formula=formula.split('+') 
splitted_formula=[]
for f in plus_split_formula:
    splitted=f.split('-')
    for ff in splitted: 
        no_zero=ff.lstrip('0')
        if no_zero != '':
            splitted_formula.append(no_zero) 
        else:
            splitted_formula.append('0')
new_formula=splitted_formula[0]
split_num=1
for f in formula: 
    if f=='+' or f=='-': 
        new_formula+=f 
        new_formula+=splitted_formula[split_num] 
        split_num+=1 
result='' 
break2=False 
start=True
for i,f in enumerate(new_formula):

    if f=='-' and start==False : 
        result += ')'
        result += f 
        start = True
        if i!=len(new_formula)-1:
            result += '('
            start=False

    elif f == '-' and start==True: 
        result += f 
        result+='(' 
        start=False

    elif i==len(new_formula)-1 and start==False:
        result += f
        result += ')'

    else:
        result+=f 
print(eval(result))
