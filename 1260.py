from collections import deque

n, m, start = map(int, input().split())
visited = [ False for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n+1):
    if graph[i]:
        graph[i].sort()


def dfs(graph, start, visited):
    x = start
    visited[x] = True
    print(x, end=' ')
    for i in graph[x]:
        if i and visited[i] == False:
            dfs(graph, i, visited)

dfs(graph, start, visited)
print()

visited = [ False for _ in range(n+1)]
q = deque()
def bfs(graph, start, visited):
    q.append(start)
    visited[q[0]] = True
    while q:
        x = q.popleft()
        print(x, end=' ')
        for i in graph[x]:
            if i and visited[i] == False:
                q.append(i)
                visited[i] = True

bfs(graph, start, visited)
