def solution(s):
    answer = []
    

    loop = 0    
    zero = 0
    
    while(len(s)>1):
        zero += s.count('0')
        s = s.replace('0', '')
        s = str(bin(int(len(s)))).replace('0b', '')
        loop += 1
        
    answer += [loop, zero]
    
    return answer