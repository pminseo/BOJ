n = int(input())
arr = list(map(int, input().split()))
c = [1]*1000001
for i in range(n):
    c[arr[i]] = 0
del c[0]
x=0
for j in c:
    x += 1
    if j == 1:
        print(x)
        break