import sys
N = int(sys.stdin.readline())
commands = list(map(str, sys.stdin.readline().split()))

x, y = 1, 1
for cmd in commands:
    if cmd == 'R':
        if y == N:
            continue
        y += 1
    elif cmd == 'L':
        if y == 1:
            continue
        y -= 1
    elif cmd == 'U':
        if x == 1:
            continue
        x -= 1
    else:
        if x == N:
            continue
        x += 1
print(x, y)
