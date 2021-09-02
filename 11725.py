import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
parents = [0 for _ in range(N+1)]

for n in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs():
    q = []
    q.append(1)
    while q:
        node = q.pop(0)
        for i in graph[node]:
            if parents[i] == 0:
                parents[i] = node
                q.append(i)
    return parents

bfs()
for i in parents[2:]:
    print(i)