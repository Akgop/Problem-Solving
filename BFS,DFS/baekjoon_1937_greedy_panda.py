import sys


def dfs(depth, x, y, n, dp):
    # 1. 상 하 좌 우 살펴봄
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        # 2. 다음 위치가 더 대나무가 많으면,
        if bamboo[nx][ny] > bamboo[x][y]:
            # 3. 다음 위치에서 갈 수 있는 값을 미리 저장해놨다면.
            if dp[nx][ny] != -1:
                # 다음값 + 1과 현재값 비교.
                dp[x][y] = max(dp[x][y], dp[nx][ny] + 1)
                continue
            dp[x][y] = max(dfs(depth + 1, nx, ny, n, dp) + 1, dp[x][y])
    if dp[x][y] == -1:
        dp[x][y] = 1
    return dp[x][y]


def solution(n):
    # 1. 전체 순회.
    dp = [[-1] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dfs(1, i, j, n, dp)
    answer = 0
    for i in range(n):
        for j in range(n):
            answer = max(dp[i][j], answer)
    return answer


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    N = int(sys.stdin.readline().rstrip())
    bamboo = []
    for _ in range(N):
        bamboo.append(list(map(int, sys.stdin.readline().split())))
    print(solution(N))

