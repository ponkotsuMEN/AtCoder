n, w = map(int, input().split())
time = [0] * 200001
for i in range(n):
    s, t, p = map(int, input().split())
    time[s] += p
    time[t] -= p
for i in range(1, n):
    time[i] += time[i-1]
if max(time) > w:
    print("No")
else:
    print("Yes")
