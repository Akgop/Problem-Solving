# O(n^2)
import sys
N = int(input())
A = list(map(int, sys.stdin.readline().split()))
result = [1] * N

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            result[i] = max(result[i], result[j]+1)
print(max(result))




