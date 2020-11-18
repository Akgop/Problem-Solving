import sys


def validation(depth, n, m):
    if depth == m:              # 탈출조건 : leaf node 달성 시 수열을 찾은 것
        print(' '.join(map(str, li)))
        return
    for i in range(n):
        if visited[i] == 0:     # 방문한적이 있는지 검사
            visited[i] = 1      # 방문 flag 를 올림
            li.append(i+1)      # stack 에 현재 노드를 추가, i+1인 이유는 indexing 때문
            validation(depth+1, n, m)   # 다음 level 탐색
            visited[i] = 0      # 탈출했을 시 해당 노드 방문이력 삭제
            li.pop()            # stack 에서 삭제


N, M = map(int, sys.stdin.readline().split())
visited = [0] * N
li = []
validation(0, N, M)



