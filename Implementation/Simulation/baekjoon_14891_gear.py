import sys


def rotate(li, di):
    if di == 1:     # 오른쪽 방향
        return li[-1:] + li[:-1]
    return li[1:] + li[:1]  # 왼쪽 방향


gears = []
for _ in range(4):
    gears.append(list(sys.stdin.readline().rstrip()))
K = int(sys.stdin.readline().rstrip())

for _ in range(K):
    gear_n, direction = map(int, sys.stdin.readline().split())
    if gear_n == 1:
        if gears[0][2] != gears[1][6]:  # 1,2 둘이 다르면 회전
            if gears[1][2] != gears[2][6]:  # 2,3 둘이 다르면 회전
                if gears[2][2] != gears[3][6]:
                    gears[3] = rotate(gears[3], -direction)
                gears[2] = rotate(gears[2], direction)
            gears[1] = rotate(gears[1], -direction)
        gears[0] = rotate(gears[0], direction)
    elif gear_n == 2:
        if gears[0][2] != gears[1][6]:  # 1,2
            gears[0] = rotate(gears[0], -direction)
        if gears[1][2] != gears[2][6]:  # 2,3
            if gears[2][2] != gears[3][6]:   # 3,4
                gears[3] = rotate(gears[3], direction)
            gears[2] = rotate(gears[2], -direction)
        gears[1] = rotate(gears[1], direction)
    elif gear_n == 3:
        if gears[2][2] != gears[3][6]:  # 3,4
            gears[3] = rotate(gears[3], -direction)
        if gears[1][2] != gears[2][6]:  # 2,3
            if gears[0][2] != gears[1][6]:   # 1,2
                gears[0] = rotate(gears[0], direction)
            gears[1] = rotate(gears[1], -direction)
        gears[2] = rotate(gears[2], direction)
    else:
        if gears[2][2] != gears[3][6]:  # 3,4
            if gears[1][2] != gears[2][6]:  # 2,3
                if gears[0][2] != gears[1][6]:  # 1,2
                    gears[0] = rotate(gears[0], -direction)
                gears[1] = rotate(gears[1], direction)
            gears[2] = rotate(gears[2], -direction)
        gears[3] = rotate(gears[3], direction)

answer = 0
for i in range(4):
    if gears[i][0] == '1':
        answer += (2**i)*1
print(answer)
