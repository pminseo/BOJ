# n, m = map(int, input().split())
# num = list(map(int, input().split()))
# arr = [0 for _ in range(n+1)]

# for i in range(n):
#     arr[i+1] = arr[i] + num[i]

# for k in range(m):
#     a, b = map(int, input().split())
#     print(arr[b] - arr[a-1])


import sys
n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
arr = [0 for _ in range(n+1)]

for i in range(n):
    arr[i+1] = arr[i] + num[i]

for k in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(arr[b] - arr[a-1])
        