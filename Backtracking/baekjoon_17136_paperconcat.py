import sys


def check(x, y, size, papers):
    # 색종이가 없는 경우
    if papers[size] == 0:
        return False
    # 보드 범위를 넘어가는 경우
    if x + size > 10 or y + size > 10:
        return False
    for i in range(x, x+size):
        for j in range(y, y+size):
            # 색종이로 0인 공간은 채울 수 없음
            if board[i][j] == 0:
                return False
    return True


def all_zero():
    for i in range(10):
        for j in range(10):
            if board[i][j] == 1:
                return False
    return True


def set_number(x, y, size, num):
    for i in range(x, x+size):
        for j in range(y, y+size):
            board[i][j] = num


def backtrack(papers):
    global answer
    # 판이 모두 0이면 answer
    if all_zero():
        answer = min(answer, 25-sum(papers))
        return
    if 25-sum(papers) > answer:
        return
    # 1의 위치를 찾음
    x, y = -1, -1
    for i in range(10):
        if x > -1:
            break
        for j in range(10):
            if board[i][j] == 1:    # 앞에서 all zero 를 검사했기에 무조건 나옴
                x, y = i, j
                break
    for size in range(len(papers)-1, 0, -1):
        if check(x, y, size, papers):
            set_number(x, y, size, 0)
            papers[size] -= 1

            backtrack(papers)

            papers[size] += 1
            set_number(x, y, size, 1)
    return


def solution():
    papers = [0, 5, 5, 5, 5, 5]
    backtrack(papers)


if __name__ == "__main__":
    board = []
    answer = 26
    for _ in range(10):
        board.append(list(map(int, sys.stdin.readline().rstrip().split())))
    solution()
    print(answer if answer < 26 else -1)
