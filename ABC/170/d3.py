from collections import Counter
n = int(input())
a = list(map(int, input().split()))
a.sort()
c = Counter(a)
m = max(a) + 1
dp = [False]*m
ans = 0
for ai in a:
    if dp[ai]:
        continue
    if c[ai] == 1:
        ans += 1
    for i in range(ai, m, ai):
        dp[i] = True
print(ans)
