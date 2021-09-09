n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

visited = [ [False for _ in range(n)] for _ in range(n)]
count = 1
lst = [0 for _ in range(n**2)]

def dfs(x, y):
    if x<0 or y<0 or x>=n or y>= n or graph[x][y] == 0:
        return False
    
    if visited[x][y] == False:
        visited[x][y] = True
        graph[x][y] = count
        lst[count] += 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
    else:
        return False

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == False:
            dfs(i, j)
            count += 1
for g in graph:
    print(g)
print(count-1)
ans = []
for l in lst:
    if l != 0:
        ans.append(l)
ans.sort()
for s in ans:
    print(s)