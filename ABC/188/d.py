n, prime = map(int, input().split())
service = []

for i in range(n):
    a, b, c = map(int, input().split())
    service.append([a, c])
    service.append([b+1, -c])
service.sort()
sum = 0
ans = 0
for i in range(2*n-1):
    sum += service[i][1]
    per_day = min(sum, prime) * (service[i+1][0] - service[i][0])
    ans += per_day

print(ans)
