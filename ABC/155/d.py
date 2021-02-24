import nnumpy as np
n, k = map(int, input().split())
a = np.array(list(map(int, input().split())))
plus = a[a > 0]
zero = a[a == 0]
minus = a[a < 0]

# ans == 0
if len(minus) * len(plus) < k:
    least = k - len(minus) * len(plus)
    if len(zero) * (k - len(zero)) + least >= k:
        print(0)
        exit()

    # ans > 0
    least = k - (len(zero) * (k - len(zero)) + least)
