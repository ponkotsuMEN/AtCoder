n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
end_a = False
end_b = False
if sum(a) + sum(b) <= k:
    print(len(a)+len(b))
    exit()
while(True):
    k -= min(a[0], b[0])
    if k >= 0:
        ans += 1
    else:
        break
    if a[0] > b[0]:
        del b[0]
    else:
        del a[0]
    if len(a) == 0:
        a = [1e9+1]
        end_a = True
    if len(b) == 0:
        b = [1e9+1]
        end_b = True
    if end_a and end_b:
        break
print(ans)
