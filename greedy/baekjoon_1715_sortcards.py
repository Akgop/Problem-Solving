import sys
import heapq


def solution(cards, n):  # 1 <= n <= 100000 -> O(NlogN) 까지 사용 가능
    if n == 1:
        return 0
    heap = list()
    # 해당 카드들을 모두 min-heap 에 저장
    for card in cards:              # O(N)
        heapq.heappush(heap, card)  # heappush: O(logN) 따라서 O(NlogN)
    result = list()
    while True:
        tmp = heapq.heappop(heap)   # 하나 뽑았을때
        if len(heap) == 0:          # 더이상 원소가 없다면 break
            break
        tmp += heapq.heappop(heap)  # 두 번째 뽑아서 더함
        heapq.heappush(heap, tmp)   # 더한 값 다시 min-heap 에 push
        result.append(tmp)          # 결과에도 push
    answer = sum(result)            # O(N)
    return answer


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    _cards = list()
    for _ in range(N):
        _cards.append(int(sys.stdin.readline().rstrip()))
    print(solution(_cards, N))
