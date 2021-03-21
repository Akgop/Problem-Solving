import sys
from collections import deque


def solution(n):
    q = deque()

    for i in range(1, n + 1):      # O(N)
        q.append(i)

    while True:
        now = q.popleft()
        if not q:
            answer = now
            break
        now = q.popleft()
        if not q:
            answer = now
            break
        q.append(now)
    print(answer)


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    solution(N)
