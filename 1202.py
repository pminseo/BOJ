import sys
input = sys.stdin.readline

n, k = map(int, input().split())
jewely = []
for i in range(n):
    jewely.append(list(map(int, input().split())))
bag = []
for j in range(k):
    bag.append(int(input()))
jewely.sort()
bag.sort()

val = 0
tmp = []

for b in bag:
    while jewely and b >= jewely[0][0]:
        tmp.append(jewely[0][1])
        jewely.pop(0)
    if tmp:
        val += tmp.pop(0)
    elif not jewely:
        break

print(val)