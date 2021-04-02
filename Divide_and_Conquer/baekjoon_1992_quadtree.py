import sys


def is_same_num(l, r, t, b):
    color = graph[t][l]
    for i in range(t, b):
        for j in range(l, r):
            if graph[i][j] != color:
                return False
    return True


def divide(left, right, top, bottom):
    # 만약 한칸만 남은 상태면
    if left == right - 1 and top == bottom - 1:
        stack.append(graph[top][left])
        return
    # 모든 타일이 같다면
    if is_same_num(left, right, top, bottom):
        stack.append(graph[top][left])
        return
    # 더 분할해야 함
    mid_lr = (left + right) // 2
    mid_tb = (top + bottom) // 2
    stack.append('(')
    divide(left, mid_lr, top, mid_tb)
    divide(mid_lr, right, top, mid_tb)
    divide(left, mid_lr, mid_tb, bottom)
    divide(mid_lr, right, mid_tb, bottom)
    stack.append(')')


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    graph = list()
    for _ in range(N):
        graph.append(list(sys.stdin.readline().rstrip()))
    stack = list()
    divide(0, N, 0, N)
    answer = ''.join(stack)
    print(answer)
