n, k = map(int, input().split())
a = list(map(int, input().split()))

loc = a[0] - 1
pre = [False] * n
pre[0] = 0
pre[loc] = 1
i = 1
while(not i == k - 1):
    i += 1
    loc = a[loc] - 1
    if pre[loc] == False:
        pre[loc] = i
    else:
        loop = i - pre[loc] + 1
        loop = (k - 1 - i) % loop
        i = k - 1 - loop
        for j in range(i, k-1):
            loc = a[loc] - 1
        print(loc + 1)
        exit()

print(loc + 1)
