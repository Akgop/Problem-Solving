import sys
from collections import deque


def solution(n, prev_ranks, m, changed):
    # 위상 정렬을 사용하기 위한 진입차수 리스트와 인접 행렬
    in_degree = [0] * (n + 1)
    graph = [[False] * (n + 1) for _ in range(n + 1)]

    # 작년 순위에 따라 -> 인접 행렬 구축, 진입차수 설정
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            graph[prev_ranks[i-1]][prev_ranks[j-1]] = True   # 간선이 있다고 저장
            in_degree[prev_ranks[j-1]] += 1    # 도착하는 노드의 진입차수 + 1

    # 변동 사항 반영
    for i in range(m):
        a, b = changed[i]
        if graph[a][b]:
            in_degree[a] += 1
            in_degree[b] -= 1
        else:
            in_degree[a] -= 1
            in_degree[b] += 1
        graph[b][a] ^= True     # 기존 연결된 노드 해제
        graph[a][b] ^= True      # 순서가 바뀐 노드 연결

    # 위상 정렬 수행해서 순서대로 출력
    q = deque()
    cycle = False
    duplicated = False
    answer = ""
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.append(i)
    for _ in range(n):
        if len(q) == 0:
            cycle = True
            break
        if len(q) >= 2:
            duplicated = True
            break
        cur = q.popleft()
        answer += str(cur) + " "
        for i in range(1, n + 1):
            # cur 에서 i 로 연결이 되어있다면 -> 연결을 끊고 진입차수를 1 줄인다.
            if graph[cur][i]:
                in_degree[i] -= 1
                # 진입차수가 0이 되버렸다면 큐에 추가한다.
                if in_degree[i] == 0:
                    q.append(i)
    if cycle:
        return "IMPOSSIBLE"
    if duplicated:
        return "?"
    return answer


if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        N = int(sys.stdin.readline().rstrip())
        Ti = list(map(int, sys.stdin.readline().rstrip().split()))
        M = int(sys.stdin.readline().rstrip())
        Changed = []
        for _ in range(M):
            Changed.append(list(map(int, sys.stdin.readline().rstrip().split())))
        print(solution(N, Ti, M, Changed))
