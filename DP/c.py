n = int(input())
init = int(pow(10, 9))
dp = [[init, init, init] for _ in range(n)]
dp[0] = list(map(int, input().split()))
for i in range(1, n):
    line = list(map(int, input().split()))
    dp[i][0] = line[0] + max(dp[i-1][1], dp[i-1][2])
    dp[i][1] = line[1] + max(dp[i-1][0], dp[i-1][2])
    dp[i][2] = line[2] + max(dp[i-1][0], dp[i-1][1])
print(max(dp[-1]))
