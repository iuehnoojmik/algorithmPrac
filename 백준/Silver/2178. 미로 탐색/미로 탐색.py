from collections import deque

n, m = map(int, input().split())
maps = []

for _ in range(n):
    maps.append(list(map(int, input())))

steps = [(0,1),(0,-1),(1,0),(-1,0)]

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
            queue.append((newRow, newCol))
            maps[newRow][newCol] += maps[row][col]

print(maps[n-1][m-1])