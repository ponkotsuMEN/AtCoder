a, b, w = map(int, input().split())
m = pow(10, 9)
M = 0
for i in range(1, 1000000+1):
    if a*i <= w*1000 <= b*i:
        m = min(m, i)
        M = max(M, i)
if M == 0:
    print("UNSATISFIABLE")
else:
    print(m, M)
