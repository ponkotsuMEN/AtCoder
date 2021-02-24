n, s = input().split()
n = int(n)
dic = {'A':0, 'T':0, 'C':0, 'G':0}
ans = 0
for i in range(n):
    dic[s[i]] += 1
    tmp = dic.copy()
    for j in range(i+1, n):
        dic[s[j]] += 1
        if dic['A'] == dic['T'] and dic['G'] == dic['C']:
            ans += 1
    dic = tmp.copy()
    dic[s[i]] -= 1
print(ans)
