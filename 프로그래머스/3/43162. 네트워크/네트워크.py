from collections import deque

def solution(n, computers):
    answer = 0
    
    isVisited = [0] * n
    queue = deque()
    
    while sum(isVisited) < n:
        answer += 1
        queue.append(isVisited.index(0))
        while queue:
            v = queue.popleft()
            # 방문하지 않은 컴퓨터일 경우
            if isVisited[v] == 0:
                isVisited[v] = 1
                for i in range(n):
                    if computers[v][i] == 1 and isVisited[i] == 0:
                        queue.append(i)
    
    return answer