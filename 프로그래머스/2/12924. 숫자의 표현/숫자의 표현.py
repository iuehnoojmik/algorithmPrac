def solution(n):

    start, end, count = 1, 1, 0
    
    while start <= n:
        if sum((range(start,end))) == n:
            count += 1
            start += 1
        elif sum((range(start,end))) > n:
            start += 1
        else:
            end += 1
            
    
    return count