import sys
from collections import deque


def solution(n, m):
    # 큐 초기화 -> (인덱스, 값)
    q = deque()
    for i in range(n):
        q.append((i, priority[i]))
    priority.sort(reverse=True)

    answer = 0
    while q:
        # 우선 하나를 뽑음
        now = q.popleft()

        # 만약 뽑았는데 큐가 비어있을 경우
        if not q:
            break

        # 뽑은게 중요도가 가장 높은 놈이 아닌 경우
        if now[1] < priority[answer]:
            q.append(now)
            continue

        # 만약 뽑은 애가 찾던 인덱스 값이라면
        if now[0] == m:
            break

        # 아니라면 다른 애가 출력 되었기 때문에 + 1
        answer += 1
    print(answer + 1)


if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        N, M = map(int, sys.stdin.readline().rstrip().split())
        priority = list(map(int, sys.stdin.readline().rstrip().split()))
        solution(N, M)
