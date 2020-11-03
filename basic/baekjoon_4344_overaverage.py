C = int(input())
for _ in range(C):
    score = list(map(int, input().split()))
    avg = sum(score[1:score[0]+1]) / score[0]
    cnt = 0
    for i in range(1, score[0]+1):
        if score[i] > avg:
            cnt += 1
    answer = round((cnt/score[0]), 5)
    print("%.3f%%" % (answer*100))

# % 자체를 출력하고 싶다면 %%로 출력
