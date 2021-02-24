n = int(input())
d, m = divmod(n, 26)
ans = ""
if m == 0:
    ans += 'z'
    d -= 1
else:
    ans += chr(m+96)

# ans = ""
while(not d==0):
    d, m = divmod(d, 26)
    if m == 0:
        ans += 'z'
        d -= 1
    else:
        ans += chr(m+96)

# ans += tmp
print(ans[::-1])
