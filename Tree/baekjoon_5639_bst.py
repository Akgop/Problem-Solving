import sys
import bisect


def solution(left, right):
    if left > right:
        return

    root = tree[left]
    # tmp = left + 1
    # while tmp <= right:
    #     if tree[tmp] > root:
    #         break
    #     tmp += 1
    tmp = bisect.bisect_left(tree, root, left+1, right+1)

    solution(left+1, tmp-1)
    solution(tmp, right)
    print(tree[left])


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    tree = []
    while True:
        try:
            tree.append(int(sys.stdin.readline()))
        except:
            break
    solution(0, len(tree)-1)
