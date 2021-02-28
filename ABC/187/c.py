n = int(input())
words = set()
for i in range(n):
    s = input()
    words.add(s)
    if s[0] == '!':
        if s[1:] in words:
            print(s[1:])
            exit()
    else:
        if '!' + s in words:
            print(s)
            exit()
print("satisfiable")
