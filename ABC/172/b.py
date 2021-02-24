s = input()
t = input()
ans = 0
for i in range(len(s)):
    if not s[i] == t[i]:
        ans += 1
print(ans)
