import sys


def change_color(n, wheel):
    new_wheel = list()
    for i in range(1, n+1):
        # 1. 색이 모두 같다면 -> 파란색
        if wheel[i-1] == wheel[i] == wheel[i+1]:
            new_wheel.append('B')
            continue
        # 2. 색이 모두 다르다면 -> 파란색
        if wheel[i-1] != wheel[i] and wheel[i] != wheel[i+1] and wheel[i-1] != wheel[i+1]:
            new_wheel.append('B')
            continue
        # 3. 빨강 두개 초록 하나 -> 빨강
        # 4. 초록 두개 파랑 하나 -> 빨강
        # 5. 파랑 두개 빨강 하나 -> 빨강
        cnt_r = wheel[i-1:i+2].count('R')
        cnt_g = wheel[i-1:i+2].count('G')
        cnt_b = wheel[i-1:i+2].count('B')
        if (cnt_r == 2 and cnt_g == 1) or (cnt_g == 2 and cnt_b == 1) or (cnt_b == 2 and cnt_r == 1):
            new_wheel.append('R')
            continue
        # 6. 나머지 경우 -> 초록
        new_wheel.append('G')
    return new_wheel


def solution(n, k, wheel):
    for _ in range(k):
        wheel = change_color(n, wheel)
        wheel.append(wheel[0])
        wheel.append(wheel[1])
    result = [0, 0, 0]
    for i in range(n):
        if wheel[i] == 'R':
            result[0] += 1
        if wheel[i] == 'G':
            result[1] += 1
        if wheel[i] == 'B':
            result[2] += 1
    return ' '.join(map(str, result))


if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    W = list(sys.stdin.readline().rstrip())
    W.append(W[0])
    W.append(W[1])
    print(solution(N, K, W))
