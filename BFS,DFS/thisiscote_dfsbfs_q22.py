from collections import deque
import heapq

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 반시계 방향 - 상 하 좌 우
rotate = [
    (1, -1), (-1, 1), (1, 1), (-1, -1),
    (-1, -1), (1, 1), (1, -1), (-1, 1)
]
rotate_right = [
    (1, 1), (-1, -1), (-1, 1), (1, -1),
    (-1, 1), (1, -1), (-1, -1), (1, 1)
]


def bfs(board, start_o, start_t, n, d):
    hq = []
    heapq.heappush(hq, (d, start_o, start_t))
    visited = [[False]*n for _ in range(n)]
    visited[start_o[0]][start_o[1]] = True
    visited[start_t[0]][start_t[1]] = True
    while hq:
        print(hq)
        dist, one, two = heapq.heappop(hq)
        print(dist, one, two)
        print(hq)
        # 종료 조건 -> one 이 (n-1, n-1)에 도달
        if one[0] == n-1 and one[1] == n-1:
            return dist
        if two[0] == n-1 and two[1] == n-1:
            return dist

        # 상하좌우 이동
        for i in range(4):
            # 두 점 모두 이동시킴
            one_nx = one[0] + dx[i]
            one_ny = one[1] + dy[i]
            two_nx = two[0] + dx[i]
            two_ny = two[1] + dy[i]
            # 인덱스 범위 초과
            if one_nx < 0 or one_ny < 0 or one_nx >= n or one_ny >= n:
                continue
            if two_nx < 0 or two_ny < 0 or two_nx >= n or two_ny >= n:
                continue
            # visited 위로 둘 다 올라감
            if visited[one_nx][one_ny] and visited[two_nx][two_ny]:
                continue
            # 하나라도 벽에 올라감
            if board[one_nx][one_ny] or board[two_nx][two_ny]:
                continue
            # 이동 가능
            visited[one_nx][one_ny] = True
            visited[two_nx][two_ny] = True
            heapq.heappush(hq, (dist+1, (one_nx, one_ny), (two_nx, two_ny)))

        # 회전 하는 경우 - one 이 축
        for i in range(4):
            # two 의 위치를 index 로 설정
            if two[0] - one[0] == dx[i] and two[1] - one[1] == dy[i]:
                print(one, two, i)
                # 반시계
                two_nx = two[0] + rotate[i][0]
                two_ny = two[1] + rotate[i][1]
                print(two_nx, two_ny)
                # 돌아간 지점이 인덱스 밖
                if two_nx < 0 or two_ny < 0 or two_nx >= n or two_ny >= n:
                    continue
                # 둘 다 방문 했던 노드
                # if visited[two_nx][two_ny] and visited[one[0]][one[1]]:
                #     continue
                # 벽에 올라감
                if board[two_nx][two_ny]:
                    continue
                # 돌아가는 경로에 벽이 있는 경우
                route_x = one[0] + rotate[i + 4][0]
                route_y = one[1] + rotate[i + 4][1]
                print(route_x, route_y)
                if board[route_x][route_y]:
                    continue
                # 가능
                visited[two_nx][two_ny] = True
                heapq.heappush(hq, (dist+1, (one[0], one[1]), (two_nx, two_ny)))
                
                # 시계 방향
                two_nx = two[0] + rotate_right[i][0]
                two_ny = two[1] + rotate_right[i][1]
                if two_nx < 0 or two_ny < 0 or two_nx >= n or two_ny >= n:
                    continue
                # 둘 다 방문 했던 노드
                # if visited[two_nx][two_ny] and visited[one[0]][one[1]]:
                #     continue
                # 벽에 올라감
                if board[two_nx][two_ny]:
                    continue
                # 돌아가는 경로에 벽이 있는 경우
                route_x = one[0] + rotate_right[i + 4][0]
                route_y = one[1] + rotate_right[i + 4][1]
                if board[route_x][route_y]:
                    continue
                # 가능
                visited[two_nx][two_ny] = True
                heapq.heappush(hq, (dist + 1, (one[0], one[1]), (two_nx, two_ny)))

        # 회전 하는 경우 - two 가 축
        for i in range(4):
            # one 의 위치를 index 로 설정
            if one[0] - two[0] == dx[i] and one[1] - two[1] == dy[i]:
                # 반시계
                print(one, two, i)
                one_nx = one[0] + rotate[i][0]
                one_ny = one[1] + rotate[i][1]
                print(one_nx, one_ny)
                # 돌아간 지점이 인덱스 밖
                if one_nx < 0 or one_ny < 0 or one_nx >= n or one_ny >= n:
                    continue
                # 둘 다 방문 했던 노드
                # if visited[one_nx][one_ny] and visited[two[0]][two[1]]:
                #     continue
                # 벽에 올라감
                if board[one_nx][one_ny]:
                    continue
                # 돌아가는 경로에 벽이 있는 경우
                route_x = two[0] + rotate[(i - 1) % 4][0]
                route_y = two[1] + rotate[(i - 1) % 4][1]
                if board[route_x][route_y]:
                    continue
                # 가능
                visited[one_nx][one_ny] = True
                heapq.heappush(hq, (dist + 1, (one_nx, one_ny), (two[0], two[1])))

                # 시계 방향
                one_nx = one[0] + rotate_right[i][0]
                one_ny = one[1] + rotate_right[i][1]
                if one_nx < 0 or one_ny < 0 or one_nx >= n or one_ny >= n:
                    continue
                # 둘 다 방문 했던 노드
                # if visited[one_nx][one_ny] and visited[two[0]][two[1]]:
                #     continue
                # 벽에 올라감
                if board[one_nx][one_ny]:
                    continue
                # 돌아가는 경로에 벽이 있는 경우
                route_x = two[0] + rotate_right[(i - 1) % 4][0]
                route_y = two[1] + rotate_right[(i - 1) % 4][1]
                if board[route_x][route_y]:
                    continue
                # 가능
                visited[one_nx][one_ny] = True
                heapq.heappush(hq, (dist + 1, (one_nx, one_ny), (two[0], two[1])))
        print()

def solution(board):
    n = len(board)
    answer = bfs(board, (0, 0), (0, 1), n, 0)
    print(answer)
    return answer


print(solution(
    [[0, 0, 0, 1, 1],
     [0, 0, 0, 1, 0],
     [0, 1, 0, 1, 1],
     [1, 1, 0, 0, 1],
     [0, 0, 0, 0, 0]]
))