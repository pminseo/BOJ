n = int(input())
cardpack = list(map(int, input().split()))
cardpack.insert(0,0)
dp = [0 for _ in range(n+1)]
dp[1] = cardpack[1]
for i in range(2, len(cardpack)):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j]+cardpack[j])
print(dp[n])
