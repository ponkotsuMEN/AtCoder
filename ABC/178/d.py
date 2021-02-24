from scipy.special import comb
s = int(input())
l = s // 3
# print(l)
mod = pow(10, 9) + 7
ans = 0
last = s % 3
for i in range(l, 0, -1):
    ans += comb(i+last-1, last, exact=True) % mod
    # print(comb(i+last-1, last, exact=True))
    # ans += pow(i, last, mod)
    ans %= mod
    last += 3
print(ans)
