n = int(input())
s = input()
sum = 0
for i, char_i in enumerate(s):
    list_j = list(range(i, n))
    for j, char_j in enumerate(s[i:]):
        if char_i==char_j:
            continue
        for k, char_k in enumerate(s[i+j:]):
            if i+j-i != i+j+k-(i+j) and char_i!=char_k and char_j!=char_k:
                sum += 1
print(sum)
