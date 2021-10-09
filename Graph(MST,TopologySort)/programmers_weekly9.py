# 100개를 다 끊어보면 -> O(100) * union-find(O(100) * O(100)) == 1000000


def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]


def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)
    parent[b] = a


def count(parent, n):
    first = parent[1]
    count = 0
    for i in range(1, n + 1):
        if parent[i] == first:
            count += 1
        else:
            count -= 1
    return abs(count)


def solution(n, wires):
    answer = n
    for exclude in range(n - 1):
        # 1. 하나씩 exclude 하면서 유니온 파인드 구함
        parent = [p for p in range(n + 1)]
        for i in range(n - 1):
            if i == exclude:
                continue
            union(wires[i][0], wires[i][1], parent)
        for i in range(1, n + 1):
            parent[i] = find(i, parent)
        # 2. 두 집단 갯수 카운트 -> 절대값 구함 min값으로 업데이트
        answer = min(count(parent, n), answer)

    return answer
