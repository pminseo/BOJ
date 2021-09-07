N, K = map(int, input().split())

dp = [100001 for _ in range(100005)]
if N < K:
    dp[N] = 0

    if N != 0:
        dp[N-1] = 1
    elif N == 0:
        dp[1] = 1
        N = 1
    for j in range(2*N, K+N+1, N):
        dp[j] = dp[j-N] + 1
    for i in range(N+1, K+2):
        if i % 2 == 0:
            dp[i] = min(dp[i//2], dp[i-1], dp[i+1]) + 1
        elif i % 2 == 1:
            dp[i] = min(dp[i-1], dp[i+1]) + 1
        dp[i] = min(dp[i], dp[i-1]+1, dp[i+1]+1)
        dp[i-1] = min(dp[i-1], dp[i]+1, dp[i-2]+1)
    print(dp[K])
elif N > K:
    print(N-K)
else:
    print(0)