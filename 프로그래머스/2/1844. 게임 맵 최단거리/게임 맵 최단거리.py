from collections import deque

def solution(maps):
    answer = 0
    
    n = len(maps)
    m = len(maps[0])
    
    steps = [(-1,0),(1,0),(0,-1),(0,1)]
    
    queue = deque([(0,0)])
    while queue:
        row, col = queue.popleft()
        
        for step in steps:
            newRow = row + step[0]
            newCol = col + step[1]
            
            if newRow<0 or newRow>=n or newCol<0 or newCol>=m:
                continue
                
            if maps[newRow][newCol] == 0:
                continue
                
            if maps[newRow][newCol] == 1:
                queue.append((newRow,newCol))
                maps[newRow][newCol] += maps[row][col]
                
    if maps[n-1][m-1] == 1:
        answer = -1
    else:
        answer = maps[n-1][m-1]
    
    return answer