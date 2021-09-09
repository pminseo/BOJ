from collections import deque

t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        w, e = q.popleft()
        visited[w][e] = True
        for d in range(4):
            nx = w + dx[d]
            ny = e + dy[d]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or graph[nx][ny] == 0:
                continue
            else:
                if visited[nx][ny] == False:
                    q.append((nx, ny))

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    count = 0
    lst = []
    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1
        lst.append((b, a))
    for i, j in lst:
        if visited[i][j] == False:
            bfs(i, j)
            count += 1
    print(count)
    
