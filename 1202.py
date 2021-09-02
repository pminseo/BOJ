import sys
input = sys.stdin.readline

n, k = map(int, input().split())

jewely = [ list(map(int, input().split())) for _ in range(n)]
bag = [ int(input()) for _ in range(k)]

jewely.sort(key=lambda x:x[1], reverse=True)
bag.sort()

sum = 0
c = 0
while bag:
    for b in bag:
        a = 0
        if not jewely:
            break
        for j in jewely:
            if j[0] <= b:
                sum += j[1]
                del bag[c]
                del jewely[a]
            elif j[0] > b:
                a += 1
            elif j == jewely[-1]:
                c += 1
print(sum)
