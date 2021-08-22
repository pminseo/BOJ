t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    lst = []
    lst.append(arr.pop())
    gap = 0
    for j in range(n-2, -1, -1):
        if j%2 == 1:
            lst.insert(0, arr.pop())
            gap = max(gap, abs(lst[0]-lst[1]))
        else:
            lst.append(arr.pop())
            gap = max(gap, abs(lst[-1]-lst[-2]))
    print(gap)
