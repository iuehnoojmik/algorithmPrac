def solution(numbers, target):
    answer = 0
    nodes = [0]
    
    for num in numbers:
        tmp = []
        for node in nodes:
            tmp.append(node+num)
            tmp.append(node-num)
        nodes = tmp
        
    for i in nodes:
        if i == target:
            answer += 1
    
    return answer