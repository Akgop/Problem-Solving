# My Code using sys.stdin.readline
import sys
arr = sys.stdin.readline().split()
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])
if c <= b:
    print(-1)
else:
    x = a // (c - b) + 1
    print(x)

# input using map
a, b, c = map(int, input().split())
if b >= c:
    print(-1)
else:
    print(a//(c-b)+1)
