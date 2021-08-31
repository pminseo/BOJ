import sys
input = sys.stdin.readline

n, k = map(int, input().split())

hole = set()

order = list(map(int, input().split()))

for i in range(n):
    hole.add(order.pop(0))
count = 0


while order:
    tmp = set()
    if len(order) < n:
        for l in range(len(order)):
            tmp.add(order.pop(0))
        c = hole^tmp
        if c:
            x = 0
            d = c & tmp     
            e = c & hole
            for j in e:
                if x == len(d):
                    break
                hole.remove(j)
                count += 1
                x += 1
            for k in d:
                hole.add(k)

    else:
        for p in range(n):
            tmp.add(order.pop(0))
        c = hole^tmp
        if c:
            d = c & tmp     
            e = c & hole
            for j in e:
                hole.remove(j)
                count += 1
            for k in d:
                hole.add(k)

print(count)