import sys


def dfs(depth, n, m):
    if depth == m:
        print(' '.join(map(str, li)))
        return
    for i in range(n):
        li.append(i+1)
        dfs(depth+1, n, m)
        li.pop()


N, M = map(int, sys.stdin.readline().split())
li = []
dfs(0, N, M)

# itertools 의 product 라이브러리를 사용하는 방법
#from itertools import product

#n, m = map(int, input().split())
#print("\n".join(list(map(" ".join, product(map(str, range(1, n+1)), repeat=m)))))