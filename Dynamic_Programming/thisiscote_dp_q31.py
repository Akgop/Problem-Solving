import sys
from collections import deque


def solution(n, m, golds):
    # 2차원 리스트로 변형
    mine = [[0] * m for _ in range(n+2)]
    for i in range(1, n+1):
        for j in range(m):
            mine[i][j] = golds.popleft()

    # 초기 값 설정
    answer = [[0] * m for _ in range(n+2)]
    for i in range(1, n+1):
        answer[i][0] = mine[i][0]

    # 점화식 사용 - bottom up
    for i in range(1, m):  # 세로로 먼저 탐색
        for j in range(1, n+1):
            answer[j][i] = max(answer[j-1][i-1], answer[j][i-1], answer[j+1][i-1]) + mine[j][i]

    maximum = 0
    for i in range(1, n+1):
        maximum = max(answer[i][m-1], maximum)

    return maximum


print(solution(
    3, 4, deque([1, 3, 3, 2, 2, 1, 4, 1, 0, 6, 4, 7])
))

print(solution(
    4, 4, deque([1, 3, 1, 5, 2, 2, 4, 1, 5, 0, 2, 3, 0, 6, 1, 2])
))