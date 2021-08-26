N, L = map(int, input().split())
num = list(map(int, input().split()))
D, tmp = list(), list()

for i in range(N-1, -1, -1):
    tmp.append(num[i])
    if len(tmp) == L:
        D.append(min(tmp))
        tmp.pop(0)
for j in range(L-1):
    D.append(min(tmp))
    tmp.pop(0)

for k in range(len(D)-1, -1, -1):
    print(D[k], end=" ")