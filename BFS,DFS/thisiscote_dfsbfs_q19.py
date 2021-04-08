""" using BFS """
import sys
from collections import deque
import copy


def operate(num1, num2, cmd):
    if cmd == 0:
        num1 += num2
    if cmd == 1:
        num1 -= num2
    if cmd == 2:
        num1 *= num2
    if cmd == 3:
        if num1 * num2 < 0:
            num1 = -(abs(num1) // abs(num2))
        else:
            num1 //= num2
    return num1


def bfs(start, op, nxt_idx):
    q = deque()
    q.append((start, op, nxt_idx))
    answer = set()
    while q:
        now = q.popleft()
        # 만약 now[1] 즉, 연산자가 더이상 남지 않았다면? -> 마지막 result 종료조건
        if sum(now[1]) == 0:
            answer.add(now[0])
            continue
        # 4번 돌며 연산 완탐
        for i in range(4):
            # 해당 연산을 할 수 있으면
            if now[1][i] > 0:
                # 사칙 연산
                result = operate(now[0], numbers[now[2]], i)
                tmp = copy.deepcopy(now[1])
                tmp[i] -= 1
                q.append((result, tmp, now[2] + 1))
    print(max(answer), min(answer))


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    numbers = list(map(int, sys.stdin.readline().rstrip().split()))
    operators = list(map(int, sys.stdin.readline().rstrip().split()))
    bfs(numbers[0], operators, 1)
