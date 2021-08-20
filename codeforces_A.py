n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    print(n-a[i]+1, end=" ")