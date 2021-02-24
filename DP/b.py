n, k = map(int, input().split())
h = list(map(int, input().split()))
dp = [pow(10, 9)] * n
dp[0] = 0
for i in range(n):
    for j in range(i+1, i+k+1):
        if j == n:
            break
        dp[j] = min(dp[j], dp[i] + abs(h[j] - h[i]))
print(dp[-1])
