import sys
import heapq


def solution(classroom, n):
    # 우선순위큐 사용
    # 입장 시간을 기준으로 정렬 해야 하는 문제
    classroom.sort(key=lambda x: (x[0], x[1]))
    max_count = 1
    heap = []
    # min-heap 을 사용하는데, 여기서 key 는 끝나는 시간으로 정렬을 해야함.
    heapq.heappush(heap, (classroom[0][1], classroom[0][0]))
    for i in range(1, n):
        while heap[0][0] <= classroom[i][0]:
            heapq.heappop(heap)
            if len(heap) == 0:      # heap 이 비어 있는 경우에 대한 예외처리
                break
        heapq.heappush(heap, (classroom[i][1], classroom[i][0]))
        tmp = len(heap)
        if tmp > max_count:     # 매 순간 min-heap 의 크기에 대한 그리디 알고리즘
            max_count = tmp
    return max_count


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    Classroom = list()
    for _ in range(N):
        Classroom.append(list(map(int, sys.stdin.readline().rstrip().split())))
    print(solution(Classroom, N))
