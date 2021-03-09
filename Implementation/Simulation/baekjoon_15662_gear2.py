import sys


def rotate(li, di):
    if di == 1:     # 오른쪽 방향
        return li[-1:] + li[:-1]
    return li[1:] + li[:1]  # 왼쪽 방향


T = int(sys.stdin.readline().rstrip())
gears = []
for _ in range(T):
    gears.append(list(sys.stdin.readline().rstrip()))
K = int(sys.stdin.readline().rstrip())

for _ in range(K):
    gear_n, direction = map(int, sys.stdin.readline().split())
    # 기준으로부터 오른쪽 상한 정하기
    lower, upper = gear_n, gear_n
    for i in range(gear_n-1, T-1):
        if gears[i][2] != gears[i+1][6]:
            upper += 1
        else:
            break
    # 기준으로부터 왼쪽 하한 정하기
    for i in range(gear_n-1, 0, -1):
        if gears[i][6] != gears[i-1][2]:
            lower -= 1
            direction = -direction
        else:
            break
    # 하한 부터 상한까지 전부 rotate
    for i in range(lower-1, upper):
        gears[i] = rotate(gears[i], direction)
        direction = -direction

answer = 0
for i in range(T):
    if gears[i][0] == '1':
        answer += 1
print(answer)
