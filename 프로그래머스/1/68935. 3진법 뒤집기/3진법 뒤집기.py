def solution(n):
    answer = 0
    
    r_three = ''
    while n>0:
        r_three = r_three + str(n % 3)
        n = n // 3
        
    three = ''.join(reversed(r_three))
    
    for i in range(len(three)):
        answer += int(three[i]) * (3**i)
        print(answer)
    
    return answer