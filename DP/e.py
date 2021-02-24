n, w = map(int, input().split())
v_max = 10**5
w_max = 10**9
dp = [[w_max] * (10**5 + 1) for _ in range(n+1)]
ans = 0
# weight, value = map(int, input().split())
# for i in range(value + 1):
#     dp[0][i] = weight
for i in range(n):
    weight, value = map(int, input().split())
    for j in range(0, v_max):
        if dp[i][j] + weight > w:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j + value] = min(dp[i][j + value], dp[i][j] + weight)

for v in range(v_max-1, 0, -1):
    if not dp[-1][v] == w_max:
        print(dp[-1][v])
        exit()
print(0)
