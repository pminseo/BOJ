n, m = map(int, input().split())
ans = []
def f(start):
    if len(ans) == m:
        for a in ans:
            print(a, end=' ')
        print()

    for i in range(start, n+1):
        if i in ans:
            continue
        else:
            ans.append(i)
            f(i+1)
            ans.pop()
f(1)


# import itertools

# n, m = map(int, input().split())
# arr = [a for a in range(1, n+1)]
# ans = list(itertools.combinations(arr, m))
# for i in ans:
#     for j in range(len(i)):
#         print(i[j], end=' ')
#     print()