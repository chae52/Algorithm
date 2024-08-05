string= input().strip()

while string != 'end':
    stack =1
    one_vowel=False
    now_consonant=False
    now_vowel=False
    is_acceptable=True
    
    for i in range(len(string)):
        
        if string[i] in 'aeiou': # 모음
            one_vowel=True
            if now_vowel: # 바로 전도 모음이었음
                stack+=1
            else:
                stack=1
                now_vowel=True
                now_consonant=False
        else: # 자음
            if now_consonant: # 바로 전도 자음이었음
                stack+=1
            else:
                now_vowel=False
                now_consonant=True 
                stack=1
        # print(string[i],now_vowel,now_consonant,stack)
            
        if stack==2 and string[i] not in 'eo' and i>0:
            if string[i-1]==string[i]:
                is_acceptable=False
                # print('eo')
        
        if stack >=3 :
            is_acceptable=False
            # print('stack3')
            break
    if one_vowel==False:
        is_acceptable=False
        # print('one_vowel')
    print('<'+string+'> is'+ (' ' if is_acceptable else ' not ')+'acceptable.')
    string= input().strip()