a, b, c, d = map(int, input().split())
if a < c and b < c:
    print("No")
elif a > d and b > d:
    print("No")
else:
    print("Yes")
