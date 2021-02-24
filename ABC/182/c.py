n = input()
k = len(n)
ans = k
for i in range(2**k):
    ans_tmp = 0
    sum = 0
    for j in range(k):
        if i >> j & 1 == 1:
            sum += int(n[j])
        else:
            ans_tmp += 1
    if sum % 3 == 0:
        # print(ans_tmp, sum)
        ans = min(ans, ans_tmp)
if ans == k:
    print("-1")
else:
    print(ans)
