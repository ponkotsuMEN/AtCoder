x = input()
l = len(x)
limit = pow(10, 10000)
count = 0
i = 0
ans = 0
while count <= limit and i + 1 < l:
    if x[i] == 'S' and x[i+1] == 'T':
        count += 1
        i += 2
        if count == limit:
            ans += l - i
            break
        continue
    i += 1
    ans += 1
if not (x[-2] == 'S' and x[-1] == 'T'):
    ans += 1
print(ans)
