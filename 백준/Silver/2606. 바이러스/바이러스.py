n = int(input())

graph = [[] for _ in range(n+1)]

pair = int(input())
for _ in range(pair):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

visited = [False] * (n+1)

from collections import deque

def bfs(graph, start, visited):
    visited[start] = True
    queue = deque([start])

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

bfs(graph, 1, visited)

count = 0
for i in range(n+1):
    if visited[i] == True:
        count += 1

print(count-1)

