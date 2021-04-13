import sys
import bisect

N, X = map(int, sys.stdin.readline().rstrip().split())
li = list(map(int, sys.stdin.readline().rstrip().split()))
left = bisect.bisect_left(li, X)
right = bisect.bisect_right(li, X)
if left == right:
    print(-1)
else:
    print(right - left)
