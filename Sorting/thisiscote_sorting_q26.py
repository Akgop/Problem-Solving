import sys
import heapq


def solution():
    answer = 0
    while hq:
        num1 = heapq.heappop(hq)
        if not hq:
            break
        num2 = heapq.heappop(hq)
        answer += num1 + num2
        heapq.heappush(hq, (num1 + num2))
    return answer


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    hq = []
    for _ in range(N):
        heapq.heappush(hq, int(sys.stdin.readline().rstrip()))
    print(solution())
