k = int(input())
if k % 2 == 0:
    print(-1)
    exit()

s = 7
for i in range(1, k+1):
    if s % k == 0:
        print(i)
        exit()
    s = (s * 10 + 7) % k
print(-1)
