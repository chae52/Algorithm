def solution(phone_book):
    answer = True
    set_book=set(phone_book)
    
    for i in range(len(phone_book)):
        for j in range(1, len(phone_book[i])):
            if phone_book[i][:j] in set_book:
                answer=False
                break
        if answer==False:
            break
    return answer