# My Code
import sys
# n = input().strip()       # 76ms
n = sys.stdin.read().strip()    # 68ms
if len(n) == 0:
    print(0)
else:
    print(n.count(' ')+1)

# sys.stdin.read() is way more faster when string gets longer
