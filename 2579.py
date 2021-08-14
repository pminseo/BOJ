# dp = []
# dp[0] = 0
# dp[1] = arr[1]
# dp[2] = arr[1] + arr[2]
# dp[3] = max(dp[1]+arr[3], dp[0]+arr[2]+arr[3])
# dp[4] = max(dp[2]+arr[4], dp[1]+arr[3]+arr[4])
# dp[5] = max(dp[3]+arr[5], dp[2]+arr[4]+arr[5])
# dp[6] = max(dp[4]+arr[6], dp[3]+arr[5]+arr[6])


n = int(input())
arr = [0]
for _ in range(n):
    arr.append(int(input()))
dp = []
dp.append(0)
dp.append(arr[1])
dp.append(arr[1] + arr[2])
if n == 1:
    print(arr[1])
elif n == 2:
    print(arr[1]+arr[2])
else:
    for i in range(3, n+1):
        dp.append(max(dp[i-2]+arr[i], dp[i-3]+arr[i-1]+arr[i]))
    print(dp[n])



# n = int(input())
# arr = [0]
# for _ in range(n):
#     arr.append(int(input()))

# if n==1:
#     print(arr[1])
# else:
#     dp = [0]*(n+1)
#     dp[1]=arr[1]
#     dp[2]=arr[1]+arr[2]

#     for i in range(3, n+1):
#         dp[i]=max(dp[i-2]+arr[i], dp[i-3]+arr[i-1]+arr[i])
#     print(dp[-1])