t = int(input())

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m or graph[x][y] == 0:
        return False
    
    if visited[x][y] == False:
        visited[x][y] = True
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x,y+1)
    else:
        return False


for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    count = 0
    lst = []
    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1
        lst.append((b,a))

    for i, j in lst:
        if visited[i][j] == False:
            dfs(i, j)
            count += 1
    print(count)