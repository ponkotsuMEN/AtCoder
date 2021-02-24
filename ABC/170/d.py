n = int(input())
a = list(map(int, input().split()))
# a = sorted(a)
a.sort()
if n == 1:
    print(1)
    exit()
if a[0] == 1:
    if a[1] == 1:
        print(0)
        exit()
    else:
        print(1)
        exit()
check = True
ans = 0
double = []
for i in range(n):
    if not i == 0:
        if a[i-1] == a[i]:
            double.append(a[i])
    for j in range(0, i):
        if not a[j] == 1:
            if a[j]*2 > a[i]:
                break
        if i == j:
            continue
        if a[i]%a[j] == 0:
            check = False
            break

    if check:
        ans += 1
        # print(i)
    check = True
# print(a)
# print(ans)
# print(double)
for i in set(double):
    ans -= a.count(i)
# ans -= len(set(double))
# ans -= len(double)
print(ans)
