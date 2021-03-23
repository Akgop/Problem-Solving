import sys
from collections import deque


def get_dist(q, target):
    dist = 0
    for i in range(len(q)):
        if q[i] == target:
            break
        dist += 1
    return dist


def solution(n, m):
    # 초기 설정
    q = deque()
    for i in range(1, n+1):
        q.append(i)

    # 탐색하며 연산 횟수 카운트
    count = 0
    for i in index:
        while True:
            # 만약 맞으면 1번 연산
            if i == q[0]:
                q.popleft()
                break
            # 아니라면 2번 연산의 거리 측정
            dist = get_dist(q, i)
            if dist <= len(q) - dist:
                q.rotate(-dist)
                count += dist
            else:
                q.rotate(len(q) - dist)
                count += len(q) - dist
    print(count)


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().rstrip().split())
    index = list(map(int, sys.stdin.readline().rstrip().split()))
    solution(N, M)
