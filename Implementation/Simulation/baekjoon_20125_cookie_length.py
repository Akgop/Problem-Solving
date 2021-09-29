import sys


def find_heart(n):
    for i in range(n):
        for j in range(n):
            if board[i][j] == '*':
                return i+2, j+1


def get_left_arm_len(x, y):
    count = 0
    while y >= 0 and board[x][y] == '*':
        count += 1
        y -= 1
    return count


def get_right_arm_len(x, y, n):
    count = 0
    while y < n and board[x][y] == '*':
        count += 1
        y += 1
    return count


def move_down(x, y, n):
    count = 0
    while x < n and board[x][y] == '*':
        count += 1
        x += 1
    return x, y, count


def solution(n):
    # 1. (1,1) 부터 탐색하다가 *을 만나면 머리 맨 꼭대기로 간주하고 아래로 움직임
    x, y = find_heart(n)
    print(x, y)
    # 2. 심장을 만나면 (상,하,좌,우 전부 * 이면) 심장 포인트 저장하고, 왼쪽, 오른쪽 팔 길이 잼.
    print(get_left_arm_len(x-1, y-2), end=' ')
    print(get_right_arm_len(x-1, y, n), end=' ')
    # 3. 허리 길이 잼. 허리 끝나는 지점 저장.
    x, y, count = move_down(x, y-1, n)
    print(count, end=' ')
    # 4. 허리 끝나는 지점에서 왼쪽 대각선아래 -> 왼쪽 다리, 오른쪽 대각선 아래 -> 오른쪽 다리
    _, _, count = move_down(x, y-1, n)
    print(count, end=' ')
    _, _, count = move_down(x, y+1, n)
    print(count)


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    board = []
    for _ in range(N):
        board.append(list(sys.stdin.readline().rstrip()))
    solution(N)
