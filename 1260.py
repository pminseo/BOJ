n, m, v = map(int, input().split())
graph = [[0]*(n+1)]*(n+1)
visit_dfs = [0]*(n+1)
order_dfs = []
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def DFS(start):
    visit_dfs[start] = 1
    order_dfs.append(start)
    for i in range(1, n+1):
        if graph[start][i] == 1 and visit_dfs[i] == 0:
            DFS(i)
DFS(v)
print(order_dfs)
