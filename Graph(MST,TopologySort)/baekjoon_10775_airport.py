import sys


def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]


def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(g, p, dock):
    entries = [0] * (g + 1)
    for i in range(1, g + 1):
        entries[i] = i

    answer = 0
    for i in range(p):
        # 해당 탑승구의 루트 노드가 0이면 더이상 도킹할 탑승구가 남지 않았다는 뜻
        root = find(dock[i], entries)
        if root == 0:
            break
        union(root, root-1, entries)
        answer += 1
    return answer


if __name__ == "__main__":
    G = int(sys.stdin.readline().rstrip())
    P = int(sys.stdin.readline().rstrip())
    Dock = []
    for _ in range(P):
        Dock.append(int(sys.stdin.readline().rstrip()))
    print(solution(G, P, Dock))
