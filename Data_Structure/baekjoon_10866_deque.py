import sys
from collections import deque


def solution(n):
    q = deque()
    for cmd in commands:
        if cmd[:9] == "push_back":
            q.append(cmd[10:])
        elif cmd[:10] == "push_front":
            q.appendleft(cmd[11:])
        elif cmd == "pop_front":
            try:
                print(q.popleft())
            except:
                print(-1)
        elif cmd == "pop_back":
            try:
                print(q.pop())
            except:
                print(-1)
        elif cmd == "size":
            print(len(q))
        elif cmd == "empty":
            if not q:
                print(1)
            else:
                print(0)
        elif cmd == "front":
            try:
                print(q[0])
            except:
                print(-1)
        elif cmd == "back":
            try:
                print(q[len(q) - 1])
            except:
                print(-1)


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    commands = list()
    for _ in range(N):
        commands.append(sys.stdin.readline().rstrip())
    solution(N)
