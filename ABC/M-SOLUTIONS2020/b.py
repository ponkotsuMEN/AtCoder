a, b, c = map(int, input().split())
k = int(input())
for i in range(k):
    if a >= b:
        b *= 2
    else:
        c *= 2

if (a < b) and (b < c):
    print("Yes")
else:
    print("No")
