from collections import deque
def solution(priorities, location):
    answer = 0
    priorities = deque(priorities)
    finished = []
    maxPriority = max(priorities)
    
    while priorities:
        temp = priorities.popleft()
        if temp != maxPriority:
            priorities.append(temp)
        else:
            finished.append(temp)
            if priorities:
                maxPriority = max(priorities)
            if location == 0:
                break       
        if location == 0:
            location = len(priorities)-1
        else:
            location -= 1
        
    answer = len(finished)
        
    return answer