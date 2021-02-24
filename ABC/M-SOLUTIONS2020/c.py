n, k = map(int, input().split())
a = list(map(int, input().split()))
score = sum(a[:k])
top = 0
for i in range(k, n):
    if a[i] > a[top]:
        print("Yes")
    else:
        print("No")
    top += 1
