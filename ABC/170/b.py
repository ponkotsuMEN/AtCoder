x, y = map(int, input().split())
if y > x*4 or y < x*2:
    print("No")
elif not y%2 == 0:
     print("No")
else:
    print("Yes")
