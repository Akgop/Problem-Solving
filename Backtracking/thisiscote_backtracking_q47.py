import sys
import copy

# 인덱스는 1부터
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]


def rotate(graph, direc, i, j, n):
    ni, nj = 0, 0
    for r in range(8):
        ni = i + dx[direc[i][j]]
        nj = j + dy[direc[i][j]]
        # 스왑 하려는 위치가 벽이거나 상어임 -> 회전
        if ni < 0 or nj < 0 or ni >= n or nj >= n or graph[ni][nj] == 17:
            direc[i][j] += 1
            if direc[i][j] > 8:
                direc[i][j] = 1
        # 스왑 가능한 위치.
        else:
            break
    return ni, nj, direc


def move_fish(graph, direc, target, n):
    for i in range(n):
        for j in range(n):
            # 이동해야 하는 물고기 위치 찾음.
            if graph[i][j] == target:
                # 스왑하려는 위치가 벽이거나 상어일 수도 있으니 체크 & 회전
                ni, nj, direc = rotate(graph, direc, i, j, n)
                # 이동(물고기 위치 스왑)
                graph[i][j], graph[ni][nj] = graph[ni][nj], graph[i][j]
                direc[i][j], direc[ni][nj] = direc[ni][nj], direc[i][j]
                return graph, direc
    return graph, direc


def move_all_fish(graph, direc, n):
    for f in range(1, 17):
        graph, direc = move_fish(graph, direc, f, n)
    return graph, direc


def move_shark(graph, direc, px, py, x, y, n):
    # 만약 이동한 위치가 인덱스 범위 밖이거나, 빈 공간일 경우 상어는 더이상 먹이를 먹을 수 없음
    if x < 0 or y < 0 or x >= n or y >= n or graph[x][y] == 0:
        return 0

    # 이전 상어의 위치를 빈 공간으로 만들어줌
    graph[px][py] = 0
    direc[px][py] = 0
    # 상어가 현재 위치의 물고기를 잡아먹음, 물고기 이동
    current_fish = graph[x][y]
    graph[x][y] = 17
    graph, direc = move_all_fish(graph, direc, n)

    nx, ny = dx[direc[x][y]], dy[direc[x][y]]
    # 다음 3가지의 sub problem 을 구함
    tmp_graph, tmp_direc = copy.deepcopy(graph), copy.deepcopy(direc)
    first = move_shark(graph, direc, x, y, x + nx, y + ny, n)
    graph, direc = copy.deepcopy(tmp_graph), copy.deepcopy(tmp_direc)

    second = move_shark(graph, direc, x, y, x + nx * 2, y + ny * 2, n)
    graph, direc = copy.deepcopy(tmp_graph), copy.deepcopy(tmp_direc)

    third = move_shark(graph, direc, x, y, x + nx * 3, y + ny * 3, n)

    return current_fish + max(first, second, third)


def solution():
    # 초기 세팅
    direc, graph, n = [], [], 4
    for _ in range(n):
        tmp = list(map(int, sys.stdin.readline().rstrip().split()))
        graph.append([tmp[0], tmp[2], tmp[4], tmp[6]])
        direc.append([tmp[1], tmp[3], tmp[5], tmp[7]])

    # 초기 상어 세팅, 물고기 이동
    first_fish = graph[0][0]
    x, y = 0, 0
    graph[x][y] = 17
    graph, direc = move_all_fish(graph, direc, n)

    nx, ny = dx[direc[x][y]], dy[direc[x][y]]

    # 상어 이동의 3가지 sub problem 의 결과를 받는다.
    tmp_graph, tmp_direc = copy.deepcopy(graph), copy.deepcopy(direc)
    first = move_shark(graph, direc, x, y, x + nx, y + ny, n)
    graph, direc = copy.deepcopy(tmp_graph), copy.deepcopy(tmp_direc)

    second = move_shark(graph, direc, x, y, x + nx*2, y + ny*2, n)
    graph, direc = copy.deepcopy(tmp_graph), copy.deepcopy(tmp_direc)

    third = move_shark(graph, direc, x, y, x + nx*3, y + ny*3, n)

    return first_fish + max(first, second, third)


if __name__ == "__main__":
    print(solution())


