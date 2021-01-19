cmd = input()
col = ord(cmd[0]) - 96
row = int(cmd[1])

# simulation 유형에서 행동좌표를 배열로 저장해서 풀어보자
steps = [
    (-2, -1), (-1, -2), (1, -2), (2, -1),
    (2, 1), (1, 2), (-1, 2), (-2, 1)
]

answer = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_col = col + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if 1 <= next_row <= 8 and 1 <= next_col <= 8:
        answer += 1
print(answer)
