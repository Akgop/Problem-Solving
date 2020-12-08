import sys
N = int(input())
li = list(map(int, sys.stdin.readline().split()))
print(min(li), max(li))
