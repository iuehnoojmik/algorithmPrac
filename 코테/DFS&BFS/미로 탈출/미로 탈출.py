from collections import deque

# 시작점(0,0) 탈출점(n-1,m-1)
n, m = map(int, input().split()) 
steps = [(-1,0), (1,0), (0,-1), (0,1)]
mazeMap = []

for _ in range(n):
    mazeMap.append(list(map(int, input())))

def bfs():
    queue = deque([(0, 0)])

    while queue:
        row, col = queue.popleft()
        
        for step in steps:
            newRow = row + step[0]
            newCol = col + step[1]

            # 맵 범위 밖이면 continue
            if newRow<0 or newRow>=n or newCol<0 or newCol>=m:
                continue
            
            # 괴물이 있는 곳이면 continue
            if mazeMap[newRow][newCol] == 0:
                continue

            # 방문하지 않은 곳만 queue에 삽입
            if mazeMap[newRow][newCol] == 1:
                queue.append((newRow, newCol))
                mazeMap[newRow][newCol] += mazeMap[row][col]

bfs()
# print(mazeMap) # 시작 위치가 3이 되지만 출구가 우하향이므로 상관없음
print(mazeMap[n-1][m-1])
