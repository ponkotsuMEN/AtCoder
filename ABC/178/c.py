n = int(input())
if n == 1:
    print(0)
    exit()
mod = pow(10, 9) + 7
tmp = (pow(9, n, mod) * 2) % mod  - pow(8, n, mod)
if tmp < 0:
    tmp += mod
ans = (pow(10, n, mod) - tmp) % mod
if ans < 0:
    ans += mod
print(ans)
