x, k, d = map(int, input().split())
time = x // d
if abs(time) > k:
    print(min(abs(x - d * k), abs(x + d * k)))
    exit()
k -= time
x -= d * time
if k % 2 == 0:
    print(abs(x))
else:
    print(min(abs(x - d), abs(x + d)))
