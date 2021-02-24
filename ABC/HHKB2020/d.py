t = int(input())
mod = 1000000007
for i in range(t):
    n, a, b = map(int, input().split())
    if a > b:
        tmp = a
        a = b
        b = tmp
    a_all = pow((n - a + 1), 2, mod)
    b_all = pow((n - b + 1), 2, mod)
    same = pow((b - a + 1), 2, mod)
    print(a_all * b_all - same * b_all)
