from collections import deque

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input())))
visited = [ [False for _ in range(n)] for _ in range(n)]

#     d, u, l, r
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# for s in range(n):
#     for w in range(n):
#         print(arr[s][w], end='')
#     print()

lst = []

def f(arr, a, b, visited, c):
    q = deque()
    q.append(a)
    q.append(b)
    while q:
        x = q.popleft()
        y = q.popleft()
        visited[x][y] = True
        if arr[x][y] == 1:
            c += 1
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx<0 or ny<0 or nx>=n or ny>=n or arr[nx][ny] == 0:
                continue
            elif visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append(nx)
                q.append(ny)
    return c

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and visited[i][j] == False:
            c = 0
            c = f(arr, i, j, visited, c)
            lst.append(c)

if len(lst) > 0:
    lst.sort()
    print(len(lst))
    for l in lst:
        print(l, end=' ')
else:
    print(0)