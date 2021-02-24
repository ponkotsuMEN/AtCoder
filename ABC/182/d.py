n = int(input())
a = list(map(int, input().split()))
dif = [a[0]]
for i in range(1, n):
    dif.append(dif[i-1] + a[i])
# print(dif)
if max(dif) <= 0:
    print(0)
    exit()

ans = 0
sum = 0
index = 0
mx = a[0]
for i in range(n):
    sum += dif[i]
    mx = max(mx, dif[i])
    # print(sum)
    # print(sum, mx)
    if i == n - 1:
        ans = max(ans, sum)
    else:
        ans = max(ans, sum + mx)
print(ans)
