import sys
N = int(input())
v = [0]*N
for i in range(N):
    v[i] = (int(sys.stdin.readline()))
if N == 1:
    print(v[0])
elif N == 2:
    print(v[0]+v[1])
elif N == 3:
    tmp = [0] * 3
    tmp[0] = v[0] + v[1]
    tmp[1] = v[1] + v[2]
    tmp[2] = v[0] + v[2]
    print(max(tmp))
else:
    result = [0] * N
    tmp = [0] * 3
    tmp[0] = v[0] + v[1]
    tmp[1] = v[1] + v[2]
    tmp[2] = v[0] + v[2]
    result[0] = v[0]
    result[1] = v[0] + v[1]
    result[2] = max(tmp)
    for i in range(3, N):
        result[i] = max(v[i-1] + result[i-3], result[i-2]) + v[i]
        result[i] = max(result[i-1], result[i])
    print(result[-1])
