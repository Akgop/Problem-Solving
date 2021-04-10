import sys

N = int(sys.stdin.readline().rstrip())
li = list(map(int, sys.stdin.readline().rstrip().split()))
li.sort()
print(li[(N - 1)//2])
