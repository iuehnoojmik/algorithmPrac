from collections import deque

n, m = map(int, input().split())
matrix = []
count = 0
move = [(-1,0), (1,0), (0,-1), (0,1)]

for i in range(n):
    lst = list(map(int, input()))
    matrix.append(lst)

def bfs(x, y, matrix):
    global n, m
    matrix[x][y] = 1
    queue = deque([(x, y)])

    while queue:
        row, col = queue.popleft()
        for step in move: # 동서남북 중 방문하지 않은 곳 큐에 삽입
            newRow = row + step[0]
            newCol = col + step[1]
            if newRow>=0 and newRow<n and newCol>=0 and newCol<m:
                if matrix[newRow][newCol] == 0:
                    queue.append((newRow, newCol))
                    matrix[newRow][newCol] = 1

for x in range(n):
    for y in range(m):
        if matrix[x][y] == 0:
            bfs(x, y, matrix)
            count += 1
        
print(count)
