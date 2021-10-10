import sys
from collections import deque


def stack_obj(cur, nxt):
    while stack[cur]:
        stack[nxt].append(stack[cur].popleft())


def move_obj(cur, nx, ny):
    for obj in stack[cur]:
        location[obj][0] = nx
        location[obj][1] = ny


def next_loc(i):
    return location[i][0] + dx[direction[i]], location[i][1] + dy[direction[i]]


def change_direc(i):
    return direction_mapped[direction[i]]


def reverse_stack(cur):
    top = stack[cur].pop()
    while stack[cur]:
        stack[top].append(stack[cur].pop())
    stack[top].appendleft(top)
    return top


def stackoverflow():
    for s in stack:
        if len(s) >= 4:
            return True
    return False


def is_bottom_of_stack(i):
    if stack[i]:
        return True
    return False


def solution(n, k):
    for count in range(1, 1001):
        for i in range(k):
            if not is_bottom_of_stack(i):
                continue
            x, y = location[i][0], location[i][1]
            nx, ny = next_loc(i)
            # 1. 파란색
            if nx < 0 or ny < 0 or nx >= n or ny >= n or board[nx][ny] == 2:
                direction[i] = change_direc(i)
                nx, ny = next_loc(i)
                if nx < 0 or ny < 0 or nx >= n or ny >= n or board[nx][ny] == 2:
                    # 갈곳 없어서 방향만 바뀌고 끝.
                    continue
            # 2. 흰색
            if board[nx][ny] == 0:
                # 2.1 일단 이동
                move_obj(i, nx, ny)
                # 2.2 다음 위치에 말이 있으면
                if chess[nx][ny] != -1:
                    stack_obj(i, chess[nx][ny])
                    chess[x][y] = -1
                # 2.3 말이 없으면 체스판의 말 이동.
                else:
                    chess[x][y] = -1
                    chess[nx][ny] = i
            # 3. 빨간색
            elif board[nx][ny] == 1:
                # 3.1 일단 이동
                move_obj(i, nx, ny)
                # 3.2 번호 뒤집기
                top = reverse_stack(i)
                # 3.3 다음 말이 있으면
                if chess[nx][ny] != -1:
                    stack_obj(top, chess[nx][ny])
                    chess[x][y] = -1
                else:
                    chess[x][y] = -1
                    chess[nx][ny] = top
            if stackoverflow():
                return count
    return -1


if __name__ == "__main__":
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    direction_mapped = {0: 1, 1: 0, 2: 3, 3: 2}
    N, K = map(int, sys.stdin.readline().split())
    board = []
    direction = []
    location = []
    stack = [deque() for _ in range(K)]
    chess = [[-1]*N for _ in range(N)]
    for _ in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    for idx in range(K):
        R, C, D = map(int, sys.stdin.readline().split())
        direction.append(D-1)
        location.append([R-1, C-1])
        chess[R-1][C-1] = idx
        stack[idx].append(idx)
    print(solution(N, K))
