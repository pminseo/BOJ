n, m = map(int, input().split())
ans = []
def f():
    if len(ans) == m:
        for a in ans:
            print(a, end=' ')
        print()

    for i in range(1, n+1):
        if i in ans:
            continue
        else:
            ans.append(i)
            f()
            ans.pop()
f()