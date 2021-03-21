import sys
from collections import deque


def solution(n):
    q = deque()
    for _ in range(n):
        cmd = sys.stdin.readline().rstrip()
        if cmd[0:4] == "push":
            q.append(int(cmd[5:]))
        elif cmd == "pop":
            try:
                print(q.popleft())
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
            if q:
                print(q[0])
            else:
                print(-1)
        elif cmd == "back":
            if q:
                print(q[len(q) - 1])
            else:
                print(-1)
        else:
            pass


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    solution(N)
