from pprint import pprint


# 해당 위치에 보가 존재해도 되는지 검사
def panel_check(pillar, panel, x, y):
    # 보가 기둥 위에 있는지
    if pillar[x - 1][y] == 1 or pillar[x - 1][y + 1] == 1:
        return True
    # 양쪽에 보가 있는지
    if y - 1 >= 0:
        if panel[x][y - 1] == 1 and panel[x][y + 1] == 1:
            return True
    # 다 아니라면
    return False


# 해당 위치에 기둥이 존재해도 되는지 검사
def pillar_check(pillar, panel, x, y):
    # 기둥이 바닥인지 검사
    if x == 0:
        return True
    # 아래에 기둥이 있는지
    if pillar[x - 1][y] == 1:
        return True
    # 왼쪽으로 보가 있는지
    if y - 1 >= 0:      # 인덱스 범위 검사
        if panel[x][y - 1] == 1:
            return True
    # 오른쪽으로 보가 있는지
    if panel[x][y] == 1:
        return True
    # 다 아니라면
    return False


def all_case(pillar, panel, n):
    for i in range(n + 1):
        for j in range(n + 1):
            if pillar[i][j] == 1:
                if not pillar_check(pillar, panel, i, j):
                    return False
            if panel[i][j] == 1:
                if not panel_check(pillar, panel, i, j):
                    return False
    return True


def solution(n, build_frame):
    # 초기 설정
    pillar = [[0]*(n+1) for _ in range(n+1)]    # 기둥은 n+1
    panel = [[0]*(n+1) for _ in range(n+1)]           # 보는 n

    # build frame 순회하며 건물 짓기
    for y, x, a, b in build_frame:
        # 기둥 설치
        if a == 0 and b == 1:
            # 가능하면
            if pillar_check(pillar, panel, x, y):
                pillar[x][y] = 1
        # 기둥 삭제
        elif a == 0 and b == 0:
            # 우선 기둥을 삭제하고
            pillar[x][y] = 0
            if not all_case(pillar, panel, n):
                pillar[x][y] = 1
            # 검사 포인트 3군데 검사
            # if not pillar_check(pillar, panel, x+1, y):
            #     pillar[x][y] = 1        # 삭제 불가능
            #     continue
            # if y - 1 >= 0:
            #     if not panel_check(pillar, panel, x+1, y-1):
            #         pillar[x][y] = 1
            #         continue
            # if not panel_check(pillar, panel, x+1, y):
            #     pillar[x][y] = 1
        # 보 설치
        elif a == 1 and b == 1:
            # 가능하면
            if panel_check(pillar, panel, x, y):
                panel[x][y] = 1
        # 보 삭제
        elif a == 1 and b == 0:
            # 우선 보를 삭제
            panel[x][y] = 0
            if not all_case(pillar, panel, n):
                panel[x][y] = 1
            # 검사 포인트 4군데
            # if not pillar_check(pillar, panel, x, y):
            #     panel[x][y] = 1
            #     continue
            # if not pillar_check(pillar, panel, x, y+1):
            #     panel[x][y] = 1
            #     continue
            # if y - 1 >= 0:
            #     if not panel_check(pillar, panel, x, y-1):
            #         panel[x][y] = 1
            #         continue
            # if not panel_check(pillar, panel, x, y+1):
            #     panel[x][y] = 1
        else:
            pass

    # 결과 담기
    answer = []
    for i in range(n+1):
        for j in range(n+1):
            if pillar[j][i] == 1:
                answer.append([i, j, 0])
            if panel[j][i] == 1:
                answer.append([i, j, 1])
    return answer


print(
    solution(
        5,
        [[1, 0, 0, 1],
         [1, 1, 1, 1],
         [2, 1, 0, 1],
         [2, 2, 1, 1],
         [5, 0, 0, 1],
         [5, 1, 0, 1],
         [4, 2, 1, 1],
         [3, 2, 1, 1]]
    )
)

print(
    solution(
        5,
        [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
    )
)

print(
    solution(
        5,
        [[0, 0, 0, 1], [0, 1, 0, 1], [0, 2, 0, 1], [0, 3, 0, 1], [0, 4, 0, 1]]
    )
)