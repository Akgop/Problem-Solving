import sys
from itertools import combinations

move = [-1, 1]


def watch(teachers, n):
    for teacher in teachers:
        x, y = teacher
        now_x, now_y = x, y
        # 위로 움직임
        while True:
            nx = now_x + move[0]
            if nx < 0 or nx >= n:
                break
            if graph[nx][y] == "O":
                break
            if graph[nx][y] == "S":
                return False
            now_x = nx
        # 아래
        now_x, now_y = x, y
        while True:
            nx = now_x + move[1]
            if nx < 0 or nx >= n:
                break
            if graph[nx][y] == "O":
                break
            if graph[nx][y] == "S":
                return False
            now_x = nx
        # 왼쪽
        now_x, now_y = x, y
        while True:
            ny = now_y + move[0]
            if ny < 0 or ny >= n:
                break
            if graph[x][ny] == "O":
                break
            if graph[x][ny] == "S":
                return False
            now_y = ny
        # 오른쪽
        now_x, now_y = x, y
        while True:
            ny = now_y + move[1]
            if ny < 0 or ny >= n:
                break
            if graph[x][ny] == "O":
                break
            if graph[x][ny] == "S":
                return False
            now_y = ny
    return True


def solution(n):
    teachers = list()
    empty = list()
    for i in range(n):
        for j in range(n):
            if graph[i][j] == "T":
                teachers.append((i, j))
            elif graph[i][j] == "X":
                empty.append((i, j))

    empty_list = combinations(empty, 3)

    for coord in empty_list:
        for c in coord:
            graph[c[0]][c[1]] = "O"
        if watch(teachers, n):
            return True
        for c in coord:
            graph[c[0]][c[1]] = "X"
    return False


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    graph = list()
    for _ in range(N):
        graph.append(list(map(str, sys.stdin.readline().rstrip().split())))
    if solution(N):
        print("YES")
    else:
        print("NO")
