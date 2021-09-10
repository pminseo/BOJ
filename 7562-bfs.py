from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
dx = [-2,-1,1,2,2,1,-1,-2]
dy = [1,2,2,1,-1,-2,-2,-1]

for _ in range(t):
    l = int(input())
    a, b = map(int, input().split())
    ex, ey = map(int, input().split())
    graph = [[0 for _ in range(l)] for _ in range(l)]
    visited = [[False for _ in range(l)] for _ in range(l)]

    q = deque()
    q.append((a, b))
    while q:
        x ,y = q.popleft()
        visited[x][y] = True
        if x == ex and y == ey:
            print(graph[x][y])
            # for g in graph:
            #     print(g)
            break
        for d in range(8):
            nx = x + dy[d]
            ny = y + dx[d]
            if nx < 0 or ny < 0 or nx >= l or ny >= l or visited[nx][ny] == True:
                continue
            else:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))