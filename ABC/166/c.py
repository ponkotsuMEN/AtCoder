n, m = map(int, input().split())
h = list(map(int, input().split()))
lst = [True for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    if h[a-1] > h[b-1]:
        lst[b-1] = False
    elif h[a-1] < h[b-1]:
        lst[a-1] = False
    else:
        lst[a-1] = False
        lst[b-1] = False
print(lst.count(True))
