import sys

# 방향 인덱스도 1부터
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]


def move_shark(n, num, k, queue):
    for i in range(n):
        for j in range(n):
            # 움직일 타겟 -> num: 상어 번호
            if num == graph[i][j][0] and graph[i][j][1] == k:
                # 4 방향 탐색
                for d in shark[num][direc[num]]:
                    nx = i + dx[d]
                    ny = j + dy[d]
                    # 다음 위치가 인덱스 범위 밖이라면
                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        continue
                    # 다음 위치에 이미 지나간 다른 상어의 흔적이 있다면
                    if graph[nx][ny][0] != 0 and graph[nx][ny][1] <= k:
                        continue
                    # 다음 위치에 갈 곳이 있다면, 반영해야 하는 리스트에 추가
                    queue.append([nx, ny, num, d])
                    return
                # 만약 4방향 모두 갈 곳이 없었다면 내 냄새가 있는 쪽으로 이동한다.
                for d in shark[num][direc[num]]:
                    nx = i + dx[d]
                    ny = j + dy[d]
                    # 다음 위치가 인덱스 범위 밖이라면
                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        continue
                    # 내 흔적을 찾아서 이동
                    if graph[nx][ny][0] == num:
                        queue.append([nx, ny, num, d])
                        return
    return


def solution(n, m, k):
    time = 1
    while time <= 1000:
        # 한바꾸 돌면서 상어 이동 시키기 (숫자가 큰 상어부터 이동 -> 이전 상어는 덮어 씌워져서 삭제됨.)
        q = []
        for i in range(m, 0, -1):
            move_shark(n, i, k, q)
        # 이동 목록 반영
        for e in q:
            nx, ny, num, d = e
            graph[nx][ny][0] = num
            graph[nx][ny][1] = k + 1
            direc[num] = d
        # 한바꾸 돌면서 1초 보내기.
        flag = False
        for i in range(n):
            for j in range(n):
                if graph[i][j][0] != 0:
                    graph[i][j][1] -= 1
                    if graph[i][j][1] == 0:
                        graph[i][j][0] = 0
        # 남은 상어가 1만 있는지 체크
        for i in range(n):
            for j in range(n):
                if graph[i][j][0] != 1 and graph[i][j][1] == k:
                    flag = True
        if not flag:
            break
        else:
            time += 1
    if time > 1000:
        time = -1
    return time


if __name__ == "__main__":
    N, M, K = map(int, sys.stdin.readline().rstrip().split())
    tmp = []
    for _ in range(N):
        tmp.append(list(map(int, sys.stdin.readline().rstrip().split())))

    graph = [[] for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if tmp[row][col] != 0:
                graph[row].append([tmp[row][col], K])
            else:
                graph[row].append([tmp[row][col], 0])

    # 상어는 1번 인덱스부터
    direc = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
    shark = [[[]] for _ in range(M + 1)]
    for s in range(1, M + 1):
        for _ in range(4):
            shark[s].append(list(map(int, sys.stdin.readline().rstrip().split())))

    print(solution(N, M, K))
