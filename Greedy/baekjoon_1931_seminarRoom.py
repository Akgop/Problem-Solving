import sys
N = int(sys.stdin.readline())
li = list()
for i in range(N):
    li.append(list(map(int, sys.stdin.readline().split())))
# 끝나는 시간을 기준으로 정렬 -> Greedy 를 사용할 수 있는 정당성
li.sort(key=lambda x: (x[1], x[0]))
upper_bound = 0  # 이미 배정된 회의실 시간의 상한(회의 끝나는 시간)
answer = 0  # 배정할 수 있는 회의 개수 정답
for i in range(N):
    if li[i][0] >= upper_bound:
        upper_bound = li[i][1]
        answer += 1
print(answer)

