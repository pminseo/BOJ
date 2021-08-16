n = int(input())
check = [0] * n
net = [[0 for _ in range(n)] for _ in range(n)]
m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    net[a-1][b-1] = 1
    net[b-1][a-1] = 1

def f(start):
    check[start] = 1
    for i in range(n):
        if net[start][i] == 1 and check[i] == 0:
            f(i)

# for i in net:
#     for j in i:
#         print(j, end=" ")
#     print()
f(0)
# print("check : {}".format(check))
count = 0
for i in check:
    if i == 1:
        count += 1
print(count - 1) 
