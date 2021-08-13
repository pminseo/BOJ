n, l = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
count = 0
def dequeue():
    data = p[0]
    del p[0]
    return data

while len(p) != 0:
    m = dequeue()
    if len(p) != 0:
        while p[0] <= m+l-1:
            dequeue()
            if len(p) == 0:
                break
    count += 1
print(count)