n = int(input())
a = list(map(int, input().split()))
s = a[0]
for i in a[1:]:
    s ^= i
for i in a:
    print(s^i, end=" ")
