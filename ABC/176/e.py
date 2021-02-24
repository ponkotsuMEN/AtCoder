h, w, m = map(int, input().split())
h_list = [0] * h
w_list = [0] * w
bomb = []
for i in range(m):
    h_tmp, w_tmp = map(int, input().split())
    h_list[h_tmp - 1] += 1
    w_list[w_tmp - 1] += 1
    bomb.append((h_tmp - 1, w_tmp - 1))
bomb = set(bomb)
mh = max(h_list)
id_h = []
for i, n in enumerate(h_list):
    if n == mh:
        id_h.append(i)

mw = max(w_list)
id_w = []
for i, n in enumerate(w_list):
    if n == mw:
        id_w.append(i)

for i in id_h:
    for j in id_w:
        if not (i, j) in bomb:
            print(mh + mw)
            exit()

print(mh + mw - 1)
