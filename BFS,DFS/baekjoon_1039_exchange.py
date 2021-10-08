import sys
from collections import deque
from itertools import combinations


def exchange(num, i, j):
    num_li = list(map(int, str(num)))
    num_li[i], num_li[j] = num_li[j], num_li[i]
    if num_li[0] == 0:
        return -1
    return int("".join(map(str, num_li)))


def solution(n, k):
    answer = -1
    comb = list(combinations([i for i in range(len(str(n)))], 2))
    que = deque()
    que_set = set()
    que.append((n, 0))
    que_set.add((n, 0))
    while que:
        cur, cnt = que.popleft()
        que_set.remove((cur, cnt))
        if cnt == k:
            answer = max(cur, answer)
            continue
        for i, j in comb:
            nxt = exchange(cur, i, j)
            if nxt == -1 or (nxt, cnt+1) in que_set:
                continue
            que.append((nxt, cnt+1))
            que_set.add((nxt, cnt+1))
    return answer


if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    print(solution(N, K))
