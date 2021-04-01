import sys


def is_one_color(l, r, t, b):
    # 모두 1인지 혹은 0인지 판별
    # 파랑이면 1, 하양이면 -1, 더 잘라야 하면 0
    color = graph[t][l]
    for i in range(t, b):
        for j in range(l, r):
            if graph[i][j] != color:
                return 0
    if color == 0:
        return -1
    return 1


def divide(left, right, top, bottom, w, b):
    # 1x1 사이즈 일 때 종료
    if left == right-1 and top == bottom-1:
        if graph[top][left] == 1:
            return 0, 1
        else:
            return 1, 0
    # 모두 같은 값일 때 종료
    color = is_one_color(left, right, top, bottom)
    if color == 1:      # 파랑
        return w, b + 1
    elif color == -1:   # 하양
        return w + 1, b
    # 4 분할
    mid_lr = (left + right) // 2
    mid_tb = (top + bottom) // 2
    tmp_w1, tmp_b1 = divide(left, mid_lr, top, mid_tb, w, b)
    tmp_w2, tmp_b2 = divide(left, mid_lr, mid_tb, bottom, w, b)
    tmp_w3, tmp_b3 = divide(mid_lr, right, top, mid_tb, w, b)
    tmp_w4, tmp_b4 = divide(mid_lr, right, mid_tb, bottom, w, b)
    return w + tmp_w1 + tmp_w2 + tmp_w3 + tmp_w4, b + tmp_b1 + tmp_b2 + tmp_b3 + tmp_b4


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    N = int(sys.stdin.readline().rstrip())
    graph = list()
    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    white = 0
    blue = 0
    white, blue = divide(0, N, 0, N, white, blue)
    print(white)
    print(blue)
