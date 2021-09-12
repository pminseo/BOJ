from collections import deque

dx = [-2, -1, +1, +2, +2, +1, -1, -2]
dy = [+1, +2, +2, +1, -1, -2, -2, -1]

def bfs(x, y, end_x, end_y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        if x == end_x and y == end_y:
            print(graph[x][y])
            break

        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < l and 0 <= ny < l and visited[nx][ny] == False:
                visited[nx][ny] = True
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))    

t = int(input())
for _ in range(t):
    l = int(input())
    graph = [[0 for _ in range(l)] for _ in range(l)]
    x, y = map(int, input().split())
    ex, ey = map(int, input().split())
    visited = [[False for _ in range(l)] for _ in range(l)]


    bfs(x, y, ex, ey)