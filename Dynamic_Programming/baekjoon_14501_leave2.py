import sys


def dfs(node, n):
    if mem[node] != -1:
        return mem[node]
    time, pay = consult[node]
    # 범위 밖이면 0 리턴
    if node + time >= n:
        if node + time == n:
            mem[node] = pay
        else:
            mem[node] = 0
        return mem[node]
    # 범위 안이면 이전 값 + 현재 값
    for i in range(node + time, n):
        if mem[i] == -1:
            mem[node] = max(mem[node], (dfs(i, n) + pay))
        else:
            mem[node] = max(mem[node], mem[i] + pay)
    return mem[node]


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    consult = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
    mem = [-1] * N
    result = 0
    for s in range(N):
        result = max(dfs(s, N), result)
    print(result)
