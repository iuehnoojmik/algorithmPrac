def solution(n): 
    step = 0
    
    while n>0:
        if n%2 == 0:
            n //= 2
        else:
            n = (n-1)/2
            step += 1
    
    return step