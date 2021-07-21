import sys


def dfs(x, y, des_x, des_y):
    if x == des_x and y == des_y:
        mem[x][y] = 1
        return mem[x][y]
    answer = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 인덱스 범위 밖
        if nx < 0 or ny < 0 or nx > des_x or ny > des_y:
            continue
        # 내리막길이 아니면
        if graph[nx][ny] >= graph[x][y]:
            continue
        # 메모이제이션 된 값이 없다면
        if mem[nx][ny] == -1:
            mem[nx][ny] = dfs(nx, ny, des_x, des_y)
        answer += mem[nx][ny]
    return answer


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    M, N = map(int, sys.stdin.readline().rstrip().split())
    graph = []
    mem = [[-1]*N for _ in range(M)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for _ in range(M):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    print(dfs(0, 0, M-1, N-1))
