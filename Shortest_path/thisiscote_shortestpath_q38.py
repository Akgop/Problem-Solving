# Floyd
def solution(n, m, comparison):
    INF = int(1e6)
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    # 초기 입력
    for c in comparison:
        graph[c[0]][c[1]] = 1

    # floyd
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    # 학생 수 카운트
    count = n
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                continue
            if graph[i][j] == INF and graph[j][i] == INF:
                count -= 1
                break
    return count


print(solution(
    6, 6, [[1, 5], [3, 4], [4, 2], [4, 6], [5, 2], [5, 4]]
))

