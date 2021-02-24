sx, sy, gx, gy = map(int, input().split())
a = (-gy - sy) / (gx - sx)
b = sy - a * sx
x = -b / a
print(x)
