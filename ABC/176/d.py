from collections import deque
import numpy as np
h, w = map(int, input().split())
ch, cw = map(int, input().split())
dh, dw = map(int, input().split())
ch -= 1
cw -= 1
dh -= 1
dw -= 1
table = []
for i in range(h):
    table.append(input())

def check(h_tmp, w_tmp, steps):
    if h_tmp < 0 or w_tmp < 0 or h_tmp >= h or w_tmp >= w:
        return False
    elif visit[h_tmp][w_tmp] <= steps:
        return False
    elif table[h_tmp][w_tmp] == '#':
        return False
    else:
        return True

q = deque()
q.append((ch, cw, 0, 0))
ans = 1000000
visit = np.full((h, w), 1000000)

while not len(q) == 0:
    now = q.popleft()
    visit[now[0]][now[1]] = min(visit[now[0]][now[1]], now[3])
    if now[0] == dh and now[1] == dw:
        ans = visit[now[0]][now[1]]
        break

    if check(now[0]+1, now[1], now[3]):
        q.appendleft((now[0]+1, now[1], now[2] + 1, now[3]))
    if check(now[0], now[1]+1, now[3]):
        q.appendleft((now[0], now[1]+1, now[2] + 1, now[3]))
    if check(now[0]-1, now[1], now[3]):
        q.appendleft((now[0]-1, now[1], now[2] + 1, now[3]))
    if check(now[0], now[1]-1, now[3]):
        q.appendleft((now[0], now[1]-1, now[2] + 1, now[3]))

    if check(now[0]+1, now[1]+1, now[3]+1):
        q.append((now[0]+1, now[1]+1, now[2] + 1, now[3]+1))
    if check(now[0]-1, now[1]+1, now[3]+1):
        q.append((now[0]-1, now[1]+1, now[2] + 1, now[3]+1))
    if check(now[0]+1, now[1]-1, now[3]+1):
        q.append((now[0]+1, now[1]-1, now[2] + 1, now[3]+1))
    if check(now[0]-1, now[1]-1, now[3]+1):
        q.append((now[0]-1, now[1]-1, now[2] + 1, now[3]+1))

    if check(now[0]+2, now[1], now[3]+1):
        q.append((now[0]+2, now[1], now[2] + 1, now[3]+1))
    if check(now[0]+2, now[1]+1, now[3]+1):
        q.append((now[0]+2, now[1]+1, now[2] + 1, now[3]+1))
    if check(now[0]+2, now[1]+2, now[3]+1):
        q.append((now[0]+2, now[1]+2, now[2] + 1, now[3]+1))
    if check(now[0]+2, now[1]-1, now[3]+1):
        q.append((now[0]+2, now[1]-1, now[2] + 1, now[3]+1))
    if check(now[0]+2, now[1]-2, now[3]+1):
        q.append((now[0]+2, now[1]-2, now[2] + 1, now[3]+1))
    if check(now[0]-2, now[1], now[3]+1):
        q.append((now[0]-2, now[1], now[2] + 1, now[3]+1))
    if check(now[0]-2, now[1]+1, now[3]+1):
        q.append((now[0]-2, now[1]+1, now[2] + 1, now[3]+1))
    if check(now[0]-2, now[1]+2, now[3]+1):
        q.append((now[0]-2, now[1]+2, now[2] + 1, now[3]+1))
    if check(now[0]-2, now[1]-1, now[3]+1):
        q.append((now[0]-2, now[1]-1, now[2] + 1, now[3]+1))
    if check(now[0]-2, now[1]-2, now[3]+1):
        q.append((now[0]-2, now[1]-2, now[2] + 1, now[3]+1))

    if check(now[0], now[1]+2, now[3]+1):
        q.append((now[0], now[1]+2, now[2] + 1, now[3]+1))
    if check(now[0]-1, now[1]+2, now[3]+1):
        q.append((now[0]-1, now[1]+2, now[2] + 1, now[3]+1))
    if check(now[0]+1, now[1]+2, now[3]+1):
        q.append((now[0]+1, now[1]+2, now[2] + 1, now[3]+1))
    if check(now[0], now[1]-2, now[3]+1):
        q.append((now[0], now[1]-2, now[2] + 1, now[3]+1))
    if check(now[0]+1, now[1]-2, now[3]+1):
        q.append((now[0]+1, now[1]-2, now[2] + 1, now[3]+1))
    if check(now[0]-1, now[1]-2, now[3]+1):
        q.append((now[0]-1, now[1]-2, now[2] + 1, now[3]+1))
if not ans == 1000000:
    print(ans)
else:
    print(-1)
