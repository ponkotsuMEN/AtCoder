
import math
s, p = map(int, input().split())
root = int(math.sqrt(p) + 1)
for i in range(1, root):
    div, mod = divmod(p, i)
    if mod == 0:
        if i + div == s:
            print("Yes")
            exit()
print("No")
