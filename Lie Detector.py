n = int(input())
arr = list()
for i in range(n):
    arr.append(input())
arr.reverse()

ans = arr[0]
for j in range(n-1):
    if arr[j] == arr[j+1]:
        arr[j+1] = 'TRUTH'
    elif arr[j] != arr[j+1]:
        arr[j+1] = 'LIE'

print(arr[-1])