def solution(n):
    answer = 0
    prev = 0
    
    if n == 0:
        answer = 0
    elif n == 1:
        answer = 1
        
    a,b = 0,1
    
    for i in range(2,n+1):
        prev = a + b
        a = b
        b = prev
            
    answer = prev % 1234567
    
    return answer