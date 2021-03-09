import sys

# My Code -> O(n)
t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    dist = y - x
    cnt = 0
    while True:
        if cnt*(cnt+1) >= dist:
            break
        cnt += 1
    lower_bound = cnt*(cnt-1)
    upper_bound = cnt*(cnt+1)
    if dist - lower_bound <= upper_bound - dist:
        result = cnt*2 - 1
    else:
        result = cnt*2
    print(result)

# Time Complexity O(1)
n = int(input())
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    a = y-x     # a = distance
    t = int(pow(a-1, 0.5))
    if t**2 < a <= t**2+t:
        print(t*2)
    else:
        print(t*2+1)
