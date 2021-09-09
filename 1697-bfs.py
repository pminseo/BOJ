from collections import deque

n,k = map(int, input().split())
arr = [0 for _ in range(100001)]

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(arr[x])
            break
        for i in (x-1, x+1, 2*x):
            if 0<= i <= 100000 and arr[i] == 0:
                arr[i] = arr[x] + 1
                q.append(i)

bfs()