# 바이토닉 수열
# [1, 2] -> 2
# [1, 2, 3, 1] -> 4
# 시작점과 끝점부터 각각 LIS 를 사용한 후 각 결과를 더하고 중복수 -1
import sys
N = int(input())
A = list(map(int, sys.stdin.readline().split()))
result = [1]*N
backward = [1]*N
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            result[i] = max(result[i], result[j]+1)
        if A[(N-1)-i] > A[(N-1)-j]:
            backward[(N-1)-i] = max(backward[(N-1)-i], backward[(N-1)-j]+1)
result = [sum(x) for x in zip(result, backward)]
print(max(result) - 1)
