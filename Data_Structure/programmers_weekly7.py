from pprint import pprint


def solution(enter, leave):
    # 0. 필요한 자료구조 생성
    len_enter = len(enter)
    answer = [0] * len_enter
    met = [[False] * (len_enter + 1) for _ in range(len_enter + 1)]
    room = set()
    enter.reverse()
    leave.reverse()

    while enter:
        # 1. 입실 & 기록
        cur = enter.pop()
        for element in list(room):
            met[cur][element] = True
        room.add(cur)

        # 2. 퇴실 - 가능한 인원 모두
        while leave and leave[-1] in room:
            room.remove(leave.pop())

    # 3. 카운트
    for i in range(1, len_enter + 1):
        for j in range(1, len_enter + 1):
            if met[i][j] or met[j][i]:
                answer[i-1] += 1

    return answer


print(solution([1,4,2,3], [2,1,3,4]))
