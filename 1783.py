n, m = map(int, input().split())
# chess = [[0 for i in range(m)] for j in range(n)]
# x = 0
# y = n-1
# chess[y][x] = 1
# chess[y-2][x+1] = 1
# chess[y-3][x+3] = 1
# for i in chess:
#     for j in i:
#         print(j, end=" ")
#     print()


# count = 0
# for i in chess:
#     for j in i:
#         if j == 1:
#             count += 1
# print("visited : {}".format(count))

if n == 1:
    print(1)
elif n == 2:
    print(min(4, (m+1)//2))
else:
    if m <= 6:
        print(min(4, m))
    else:
        print(m-2)