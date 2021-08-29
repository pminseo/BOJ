n = int(input())
arr = [[0 for j in range(i+1)] for i in range(n)]
# for i in range(n):
#     for j in range(i+1):
#         print(arr[i][j], end=" ")
#     print()

for k in range(n):
    arr[k] = list(map(int, input().split()))

D = [[0 for j in range(i+1)] for i in range(n)]
D[0][0] = arr[0][0]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            D[i][j] = D[i-1][0] + arr[i][j]
        elif j == i:
            D[i][j] = D[i-1][j-1] + arr[i][j]
        else:
            D[i][j] = arr[i][j] + max(D[i-1][j-1], D[i-1][j])
print(max(D[n-1]))
