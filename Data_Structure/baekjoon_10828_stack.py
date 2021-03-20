import sys


def solution(n):
    stack = list()
    for cmd in commands:
        if cmd[0:4] == 'push':
            stack.append(int(cmd[5:]))
        if cmd == 'pop':
            try:
                print(stack[len(stack)-1])
                stack.pop()
            except:
                print(-1)
        if cmd == 'size':
            print(len(stack))
        if cmd == 'empty':
            if stack:
                print(0)
            else:
                print(1)
        if cmd == 'top':
            if not stack:
                print(-1)
            else:
                print(stack[len(stack)-1])


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    commands = list()
    for _ in range(N):
        commands.append(sys.stdin.readline().rstrip())
    solution(N)
