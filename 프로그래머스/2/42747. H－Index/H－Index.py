def solution(citations):
    maximum = max(citations)
    
    thesises = [0] * (maximum + 1)
    
    for citation in citations:
        thesises[citation] += 1
        
    cumulative = 0
    for i in range(maximum, -1, -1):
        cumulative += thesises[i]
        thesises[i] = cumulative
    
    answer = 0
    for i in range(maximum, -1, -1):
        if i <= thesises[i]:
            answer = i
            break
    
    return answer