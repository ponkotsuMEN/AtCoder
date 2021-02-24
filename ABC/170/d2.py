n = int(input())
tmp = list(map(int, input().split()))
ans = 0
a = sorted(tmp)
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
double = set(a)
for i in double:
    if not tmp.count(i) == 1:
        ans -= tmp.count(i)

# a.sort()


check = True
loop = list(range(len(a)))
for i in loop:
    for j in range(0, i):
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

print(ans)
