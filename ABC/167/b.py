a, b, c, k = map(int, input().split())
ans = 0
if a >= k:
    print(k)
    exit()
ans += a
k -= a
if b >= k:
    print(ans)
    exit()
k -= b
ans -= k
print(ans)
