import collections
n = int(input())
a = list(map(int, input().split()))
cnt = collections.Counter(a)
s = sum(a)
q = int(input())
for i in range(q):
    b, c = map(int, input().split())
    s += cnt[b]*(c-b)
    print(s)
    cnt[c] += cnt[b]
    cnt[b] = 0
