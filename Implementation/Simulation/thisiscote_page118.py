import sys


def turn_left(direction):
    direction -= 1
    if direction == -1:
        direction = 3
    return direction


N, M = map(int, sys.stdin.readline().split())
x, y, di = map(int, sys.stdin.readline().split())
visited = [[0] * M for _ in range(N)]
loc = list()
for i in range(N):
    loc.append(list(map(int, sys.stdin.readline().split())))

# 방향 설정을 해서 이동하는 문제는 별도의 리스트를 만들어서 푸는 습관
dx = [-1, 0, 1, 0]  # L D R U
dy = [0, 1, 0, -1]  # L D R U

visited[x][y] = 1  # 시작 위치 방문 표시
turn_count = 0
answer = 1
while True:
    # Step 1. 회전
    di = turn_left(di)
    next_x = x + dx[di]
    next_y = y + dy[di]
    # Step 2-1. 가보지 않은 육지라면 이동
    if visited[next_x][next_y] == 0 and loc[next_x][next_y] == 0:
        visited[next_x][next_y] = 1
        x = next_x
        y = next_y
        answer += 1
        turn_count = 0
        continue
    # Step 2-2. 가본 육지이거나 바다
    else:
        turn_count += 1
    # Step 3. 종료 조건: 모두 가본 육지
    if turn_count == 4:
        # 3-1 뒤로 가기
        next_x = x - dx[di]
        next_y = y - dy[di]
        if loc[next_x][next_y] == 0:
            x = next_x
            y = next_y
            turn_count = 0
        # 뒤로 못가는 경우
        else:
            break
print(answer)
