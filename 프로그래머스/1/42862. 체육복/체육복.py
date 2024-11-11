def solution(n, lost, reserve): 
    lost.sort()
    reserve.sort()
    answer = n - len(lost)
    
    duplicates = []
    for i in range(len(lost)):
        if lost[i] in reserve:
            duplicates.append(lost[i])
    
    for duplicate in duplicates:
        lost.remove(duplicate)
        reserve.remove(duplicate)
    
    answer += len(duplicates)
            
    for i in range(len(lost)):
        if lost[i]-1 in reserve:
            reserve.remove(lost[i]-1)
            answer += 1
        elif lost[i]+1 in reserve:
            reserve.remove(lost[i]+1)
            answer += 1
             
    return answer