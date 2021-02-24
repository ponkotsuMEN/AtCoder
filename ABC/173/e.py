n, k = map(int, input().split())
a = list(map(int, input().split()))
mod = pow(10, 9) + 7
ans = 1
for i in range(k):
    ans *= a[i]
# ans %= mod

tmp = ans
index = 0
for i in range(k, n):

    tmp /= a[index]
    # tmp %= mod
    tmp *= a[i]
    # tmp %= mod
    index += 1
    ans = max(tmp, ans)
print(int(ans % mod))
