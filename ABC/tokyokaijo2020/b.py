a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())
dis = abs(a - b)
sb = v - w
if sb <= 0:
    print("NO")
    exit()
time = dis / sb
if time > t:
    print("NO")
else:
    print("YES")
