import sys
N = int(input())
arr = []
result = [1] * N
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))
arr.sort(key=lambda x: x[0])
for i in range(N):
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            result[i] = max(result[i], result[j]+1)
answer = (max(result))
print(N - answer)
