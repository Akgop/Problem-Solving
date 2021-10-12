import sys
from collections import deque


def bfs(color, start, visited):
    result = [[start[0], start[1]]]
    que = deque()
    que.append([start[0], start[1]])
    visited[start[0]][start[1]] = True
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= 12 or ny >= 6 or visited[nx][ny] or board[nx][ny] != color:
                continue
            visited[nx][ny] = True
            result.append([nx, ny])
            que.append([nx, ny])
    if len(result) >= 4:
        return result
    return []


def move_down():
    for j in range(6):
        for i in range(11, 0, -1):
            if board[i][j] == '.':
                for k in range(1, i+1):
                    if board[i-k][j] != '.':
                        board[i][j], board[i-k][j] = board[i-k][j], board[i][j]
                        break


def solution():
    pop_chain = 0
    while True:
        visited = [[False]*6 for _ in range(12)]
        # 1. BFS 이용해서 동시에 터지는 리스트 받아오기
        will_pop = []
        for i in range(12):
            for j in range(6):
                if board[i][j] != '.' and not visited[i][j]:
                    popped = bfs(board[i][j], (i, j), visited)
                    if popped:
                        will_pop += popped
        # 1.1 터트릴 블럭이 하나도 없으면 아웃
        if not will_pop:
            break
        # 2. 리스트에 있는 블록 전부 .으로 바꿈
        for x, y in will_pop:
            board[x][y] = '.'
        # 3. 중력에 의해 블록 다 아래로 내림
        move_down()
        pop_chain += 1
    return pop_chain


if __name__ == "__main__":
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    board = []
    for _ in range(12):
        board.append(list(sys.stdin.readline().rstrip()))
    print(solution())
