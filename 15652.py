n, m = map(int, input().split())
ans = []

def f(start):
    if len(ans) == m:
        for a in ans:
            print(a, end=' ')
        print()
        return

    for i in range(start, n+1):
        ans.append(i)
        f(i)
        ans.pop()
f(1)