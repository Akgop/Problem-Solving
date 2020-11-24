import sys

N, K = map(int, sys.stdin.readline().split())
A = []
count = 0
answer = 0
for _ in range(N):
    A.append(int(sys.stdin.readline()))
while True:
    if answer == K:
        break
    temp = (K - answer)//A[-1]  # 시간 단축을 위해 count
    if temp > 0:
        answer += A[-1]*temp    # 시간 단축을 위해
        count += temp
        continue
    A.pop()
print(count)
