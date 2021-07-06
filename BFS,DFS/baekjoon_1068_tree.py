import sys


def dfs(node, leaf_count, node_to_del):
    if node == node_to_del:
        return leaf_count
    if not tree[node]:
        return leaf_count + 1
    for i in range(len(tree[node])):
        leaf_count = dfs(tree[node][i], leaf_count, node_to_del)
    return leaf_count


def solution(node_to_del):
    leaf_node = 0
    for root in roots:
        leaf_node += dfs(root, leaf_node, node_to_del)
    return leaf_node


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    parent = list(map(int, sys.stdin.readline().rstrip().split()))
    node_to_delete = int(sys.stdin.readline().rstrip())
    tree = [[] for _ in range(N)]
    roots = []
    for i in range(N):
        if parent[i] == -1:
            roots.append(i)
            continue
        if i == node_to_delete:
            continue
        tree[parent[i]].append(i)
    print(solution(node_to_delete))
