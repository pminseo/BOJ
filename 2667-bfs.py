from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
visited = [[False for _ in range(n)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
x, y = 0, 0
count = 1

def bfs(graph, a,b, visited):
    q = deque()
    q.append(a)
    q.append(b)
    while q:
        x = q.popleft()
        y = q.popleft()
        graph[x][y] = count
        visited[x][y] = True
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >= n or ny >= n or graph[nx][ny] == 0:
                continue
            else:
                if visited[nx][ny] == False:
                    q.append(nx)
                    q.append(ny)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == False:
            bfs(graph, i, j, visited)
            count += 1

lst = [0 for _ in range(count)]
for g in graph:
    for l in range(1, count):
        for h in g:
            if l == h:
                lst[l] += 1
lst.remove(0)
lst.sort()

print(count-1)
for w in lst:
    print(w)

# for o in graph:
#     print(o)
# 56% 