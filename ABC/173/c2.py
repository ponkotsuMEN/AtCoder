h, w, k = map(int, input().split())
c = [list(input()) for _ in range(h)]
ans = 0
for maskR in range((1 << h) - 1):
    for maskC in range((1 << w) - 1):
        black = 0
        for i in range(h):
            for j in range(w):
                if ((maskR >> i) & 1) == 0 and ((maskC >> j) & 1) == 0:
                    if c[i][j] == '#':
                        black += 1
        if black == k:
            ans += 1
print(ans)
