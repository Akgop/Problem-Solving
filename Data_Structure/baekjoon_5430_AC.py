import sys
from collections import deque


def solution(func, n, nums):
    q = deque(nums)
    front_flag = 1
    for f in func:
        # 순서 뒤집는 함수
        if f == 'R':
            front_flag *= -1
        # 첫번째 버리는 함수
        if f == 'D':
            try:
                if front_flag > 0:
                    q.popleft()
                else:
                    q.pop()
            except:
                print("error")
                return
    # 정상 출력
    # 해당 포맷 응용하기 print('[' + ','.join(q) + ']')
    if not q:
        print('[]')
    elif front_flag > 0:
        print('[' + ','.join(q) + ']')      # deque 도 넣을 수 있음
    else:
        q.reverse()
        print('[' + ','.join(q) + ']')


if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        P = sys.stdin.readline().rstrip()
        N = int(sys.stdin.readline().rstrip())
        if N:
            X = list(map(str, sys.stdin.readline().rstrip()[1:-1].split(',')))
        else:
            _ = input()
            X = list()
        solution(P, N, X)
