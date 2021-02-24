n = int(input())
a = list(map(int, input().split()))
pre = a[0]
ans = 0
for i in range(1, n):
    if a[i] < pre:
        ans += pre - a[i]
    else:
        pre = a[i]
print(ans)
