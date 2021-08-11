import sys


def get_max(n):
    answer = 0

    # 가로, 세로
    for i in range(n):
        row_cnt = col_cnt = 1
        for j in range(1, n):
            if board[i][j-1] == board[i][j]:
                col_cnt += 1
            else:
                answer = max(answer, col_cnt)
                col_cnt = 1

            if board[j-1][i] == board[j][i]:
                row_cnt += 1
            else:
                answer = max(answer, row_cnt)
                row_cnt = 1
        answer = max(answer, row_cnt, col_cnt)
    return answer


def solution(n):
    answer = 0
    for i in range(n):
        for j in range(n):
            for d in range(2):
                x = i + dx[d]
                y = j + dy[d]
                if x < 0 or y < 0 or x >= n or y >= n:
                    continue
                if board[i][j] == board[x][y]:
                    continue
                board[i][j], board[x][y] = board[x][y], board[i][j]     # swap
                answer = max(answer, get_max(n))
                board[i][j], board[x][y] = board[x][y], board[i][j]  # swap
    print(answer)


if __name__ == "__main__":
    dx = [1, 0]
    dy = [0, 1]
    N = int(sys.stdin.readline().rstrip())
    board = []
    for _ in range(N):
        board.append(list(sys.stdin.readline().rstrip()))
    solution(N)
