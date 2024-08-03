import math

def solution(brown, yellow):
    
    b = -((brown/2)+2)
    c = brown+yellow
    
    m = (-b + math.sqrt((b**2)-(4*c)))/2
    n = (brown+yellow)/m
    
    answer = [m, n]
    return answer
