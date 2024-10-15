# https://programmers.co.kr/learn/courses/30/lessons/72410
def solution(id):
    answer = ''

    #1단계
    id=id.lower()
    
    #2단계
    iid=''
    for i in id:
        if i=='.' or i=='-' or i=='_' or 97<=ord(i)<=122 or 48<=ord(i)<=57:
            iid+=i
    
    #3단계
    iiid = list()
    cnt = 0
    for i in range(0,len(iid)):
        if iid[i] != '.':
            iiid.append(iid[i])
            cnt=0
        elif iid[i] == '.' and cnt == 0:
            iiid.append(iid[i])
            cnt+=1
        else:
            cnt+=1
    iiid="".join(iiid)
    
    # 4단계
    if len(iiid)>0 and iiid[0]=='.':
        iiid=iiid[1:]
    if len(iiid)>0 and iiid[-1]=='.':
        iiid=iiid[0:-1]
    
    # 5단계
    if len(iiid)==0:
        iiid='a'
    
    # 6단계
    if len(iiid)>=16:
        iiid=iiid[0:15]
        if iiid[14]=='.':
            iiid=iiid[0:14]
    
    # 7단계
    if len(iiid)==2:
        iiid+=iiid[1]
    elif len(iiid)==1:
        iiid+=iiid[0]*2
        
    return iiid
