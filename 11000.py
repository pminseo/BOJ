n = int(input())
arr = []
for _ in range(n):
    start, end = map(int, input().split())
    arr.append((start, end))
arr.sort()
que = []
que.append(arr[0][1])
for i in range(1, n):
    for j in range(len(que)):
        if que[j] > arr[i][0]:
            que.append(arr[i][1])
        else:
            que[j] = arr[i][1]
            break
print(len(que))