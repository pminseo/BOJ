from collections import deque

m, n = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1,1 ,0,0]
dy = [0,0,-1,1]

def bfs():
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            else:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append([nx, ny])

                    

queue  = deque([])   
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])

bfs()
ans = 0
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit()
        else:
            ans = max(ans, j)
print(ans -1)