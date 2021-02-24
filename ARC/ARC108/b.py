n = int(input())
s = input()
i = 0
pre = 0
cnt = 0
stack = []
for i in range(n):
    stack.append(s[i])
    try:
        if stack[-3:] == ['f', 'o', 'x']:
            stack.pop()
            stack.pop()
            stack.pop()
    except:
        pass
print(len(stack))
