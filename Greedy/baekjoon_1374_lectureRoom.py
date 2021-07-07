import sys
import heapq


def solution(n):
    lec_room = []
    heapq.heappush(lec_room, 0)
    lec_info.sort(key=lambda x: x[1])
    for lec_num, lec_start, lec_end in lec_info:
        # 남는 강의 실이 있다면
        if lec_room[0] <= lec_start:
            heapq.heappop(lec_room)     # 남는 강의실 pop
            heapq.heappush(lec_room, lec_end)   # 새로 배정받은 강의의 끝나는 시간을 넣어줌
        # 남는 강의 실이 없다면
        else:
            heapq.heappush(lec_room, lec_end)
    return len(lec_room)


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    lec_info = []
    for _ in range(N):
        lec_info.append(list(map(int, sys.stdin.readline().rstrip().split())))
    print(solution(N))
