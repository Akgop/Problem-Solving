from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start, board, visited):
    que = deque()
    que.append(start)
    visited[start[0]][start[1]] = True
    n = len(board)
    min_x, min_y, max_x, max_y = n, n, -1, -1
    count = 0
    while que:
        x, y = que.popleft()
        count += 1
        if x < min_x:
            min_x = x
        if y < min_y:
            min_y = y
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny]:
                continue
            if board[nx][ny] == 0:
                visited[nx][ny] = True
                que.append((nx, ny))

    piece = [[] for _ in range(max_x+1-min_x)]
    idx = 0
    for i in range(min_x, max_x+1):
        for j in range(min_y, max_y+1):
            piece[idx].append(board[i][j])
        idx += 1
    return count, piece


def get_pieces(board):
    result = [[] for _ in range(7)]
    n = len(board)
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0 and not visited[i][j]:
                count, piece = bfs((i, j), board, visited)
                result[count].append(piece)
    return result


def turn_right(a):
    row_length = len(a)
    column_length = len(a[0])
    result = [[0] * row_length for _ in range(column_length)]
    for r in range(row_length):
        for c in range(column_length):
            result[c][row_length - 1 - r] = a[r][c]
    return result


def check(board, table, size):
    result = 0
    if not board or not table:
        return result

    flag = False
    used = [False] * len(table)
    for i in range(len(board)):
        for j in range(len(table)):
            if used[j]:
                continue
            for r in range(4):
                if board[i] == table[j]:
                    used[j] = True
                    result += size
                    flag = True
                    break
                table[j] = turn_right(table[j])
            if flag:
                flag = False
                break
    return result


def solution(game_board, table):
    # 1. 조각을 구한다.
    game_pieces = get_pieces(game_board)
    for i in range(len(table)):
        for j in range(len(table)):
            table[i][j] ^= 1
    table_pieces = get_pieces(table)

    # 2. 사이즈별로 분류된 조각을 하나씩 맞춰본다.
    answer = 0
    for size in range(1, 7):
        answer += check(game_pieces[size], table_pieces[size], size)

    return answer


print(solution(
    [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],
    [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]))