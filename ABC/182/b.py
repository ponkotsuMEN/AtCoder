n = int(input())
a = list(map(int, input().split()))
mx = 0
ans = 1
for i in range(2, max(a)+1):
    num = 0
    for j in a:
        if j % i == 0:
            num += 1
    # print(i, num)
    if mx < num:
        mx = num
        ans = i
print(ans)
