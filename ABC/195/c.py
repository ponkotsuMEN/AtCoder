n = input()
digit = len(n)
comma = digit // 3
ans = 0
for i in range(1, comma+1):
    ans += int(n) - pow(10, i*3) + 1
print(ans)
