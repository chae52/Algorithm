def solution(diffs, times, limit):
    answer = 0
    lo=1
    hi=100000
    
    while lo<=hi:
        mid=(lo+hi)//2
        
        if is_possible(mid, diffs, times, limit):
            answer=mid
            hi=mid-1
        else:
            lo=mid+1
        
    return answer

def is_possible(mid, diffs, times, limit):
    used_time=0
    for i in range(len(diffs)):
        if diffs[i]<=mid:
            used_time+=times[i]
        else:
            used_time+=(diffs[i]-mid)*(times[i]+times[i-1])+times[i]
    if used_time<=limit:
        return True
    else:
         return False