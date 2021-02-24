n, w = map(int, input().split())
dp = [[0] * (w+1) for _ in range(n)]
weight, value = map(int, input().split())
for i in range(weight, w+1):
    dp[0][i] = value
for i in range(n-1):
    weight, value = map(int, input().split())
    for j in range(0, w+1):
        if j < weight:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = max(dp[i][j], dp[i][j - weight] + value)

print(dp[-1][-1])
