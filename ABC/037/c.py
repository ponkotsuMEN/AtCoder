n, k = map(int, input().split())
a = list(map(int, input().split()))
s = sum(a[:k])
tmp = s
for i in range(1, n - k + 1):
    tmp += a[i + k - 1] - a[i - 1]
    s += tmp
print(s)
