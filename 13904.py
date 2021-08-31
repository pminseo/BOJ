n = int(input())
arr = [0 for _ in range(n)]
score = [ 0 for _ in range(1000)]

for i in range(n):
    arr[i] = list(map(int, input().split()))
    
arr.sort(key=lambda x:x[1], reverse=True)

for i in range(n):
    for j in range(arr[i][0]-1, -1, -1):
        if score[j] == 0:
            score[j] = arr[i][1]
            break

print(sum(score))