import sys


def is_one_color(l, r, t, b):
    color = graph[t][l]
    for i in range(t, b):
        for j in range(l, r):
            if graph[i][j] != color:
                return 2
    return color


def divide(left, right, top, bottom, m, z, p):
    # 1x1 사이즈
    if left == right - 1 and top == bottom - 1:
        if graph[top][left] == -1:
            m, z, p = 1, 0, 0
        elif graph[top][left] == 0:
            m, z, p = 0, 1, 0
        else:
            m, z, p = 0, 0, 1
        return m, z, p

    # 검사
    color = is_one_color(left, right, top, bottom)
    if color == -1:
        return m + 1, z, p
    elif color == 0:
        return m, z + 1, p
    elif color == 1:
        return m, z, p + 1
    else:
        # 3등분(내적)
        one_third_lr = (left * 2 + right) // 3
        two_third_lr = (left + right * 2) // 3
        one_third_tb = (top * 2 + bottom) // 3
        two_third_tb = (top + bottom * 2) // 3
        cuts = [
            (left, one_third_lr, top, one_third_tb),
            (one_third_lr, two_third_lr, top, one_third_tb),
            (two_third_lr, right, top, one_third_tb),
            (left, one_third_lr, one_third_tb, two_third_tb),
            (one_third_lr, two_third_lr, one_third_tb, two_third_tb),
            (two_third_lr, right, one_third_tb, two_third_tb),
            (left, one_third_lr, two_third_tb, bottom),
            (one_third_lr, two_third_lr, two_third_tb, bottom),
            (two_third_lr, right, two_third_tb, bottom)
        ]
        # 분할
        answer = [0, 0, 0]
        for cut in cuts:
            tmp1, tmp2, tmp3 = divide(cut[0], cut[1], cut[2], cut[3], m, z, p)
            answer[0] += tmp1
            answer[1] += tmp2
            answer[2] += tmp3
        return m + answer[0], z + answer[1], p + answer[2]


def solution(n):
    minus, zero, plus = 0, 0, 0
    minus, zero, plus = divide(0, n, 0, n, minus, zero, plus)
    print(minus)
    print(zero)
    print(plus)


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    N = int(sys.stdin.readline().rstrip())
    graph = list()
    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    solution(N)
