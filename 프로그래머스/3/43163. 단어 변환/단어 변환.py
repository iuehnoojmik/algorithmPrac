from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    words.append(begin)
    
    n = len(words) # 단어 개수
    length = len(words[0]) # 단어 길이
    graph = [[] for _ in range(n)]
    isVisited = [0] * n
    missCount = 0
    
    # 인접리스트
    for i in range(n):
        for j in range(n):
            missCount = 0
            if i == j: # 자기 자신은 pass
                continue
            for c in range(length):
                if words[i][c] != words[j][c]:
                    missCount += 1
            if missCount == 1:
                graph[i].append(j) # words[j]의 인덱스 삽입
            
    beginIndex = words.index(begin)
    targetIndex = words.index(target)        
    
    queue = deque()
    queue.append(beginIndex)
    isVisited[beginIndex] = 1
    while queue:
        v = queue.popleft()        
        for g in graph[v]:
            if isVisited[g] == 0:
                queue.append(g)
                isVisited[g] = isVisited[v] + 1
                
    if isVisited[targetIndex] == 0:
        return 0
    else:
        return isVisited[targetIndex]-1
