import math

def solution(progresses, speeds):
    answer = []
    
    queue = [math.ceil((100-i)/j) for i, j in zip(progresses, speeds)]
    
    day = queue[0]
    queue.pop(0)
    
    a = 1
    
    while len(queue)>0:
        if queue[0]>day:
            day = queue[0]
            answer.append(a)
            a = 1
        else:
            a += 1
        
        queue.pop(0)
    
    answer.append(a)
    return answer