N, K = map(int, input().split())
# list comprehension 을 이용하여 입력 여러개 받기
A = [int(input()) for _ in range(N)]

answer = 0
i = -1          # 음수 인덱싱은 뒤에서부터 탐색
while K > 0:
    answer += K // A[i]
    K %= A[i]
    i -= 1
print(answer)
