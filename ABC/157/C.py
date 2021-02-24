n, m = map(int, input().split())
num = [-1 for _ in range(n)]
for i in range(m):
    s, c = map(int, input().split())
    if not num[s-1] == -1 and not num[s-1] == c:
        print(-1)
        exit()
    num[s-1] = c
# print(num)
count = 0
for i in range(n):
    if num[i] == 0 or num[i] == -1:
        count += 1
# print(count)
if count == n:
    print(0)
    exit()
if num[0] == -1 or num[0] == 0:
    print(-1)
    exit()

for i in range(n):
    if not num[i] == -1:
        print(num[i], end="")
    else:
        print(0, end="")
print("")
