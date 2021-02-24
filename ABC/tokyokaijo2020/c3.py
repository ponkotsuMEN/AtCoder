n, k = map(int, input().split())
a = list(map(int, input().split()))

if k >= n:
    for i in range(n-1):
        print(n, end=" ")
    print(n)
    exit()
least_l = a.copy()
least_r = a.copy()
for _ in range(k):
    list = [1]*n
    for i in range(n):
        list[i] += 

    a = list.copy()
    for i in range(n-1):
        print(a[i], end=" ")
    print(a[-1])
