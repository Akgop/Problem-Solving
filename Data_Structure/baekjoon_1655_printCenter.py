import sys
import heapq


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    leftMaxHeap, rightMinHeap = [10001], [10001]
    leftCnt, rightCnt = 0, 0
    for i in range(N):
        num = int(sys.stdin.readline().rstrip())
        # 새로운 값이 들어가야할 위치 선정
        # 오른쪽보다 작거나 같으면 왼쪽에 삽입
        if num <= rightMinHeap[0]:
            heapq.heappush(leftMaxHeap, -num)
            leftCnt += 1
        # 아니라면 오른쪽에 삽입
        else:
            heapq.heappush(rightMinHeap, num)
            rightCnt += 1
        # 왼쪽,오른쪽 노드 개수 밸런싱
        if leftCnt - rightCnt == 2:
            tmp = -heapq.heappop(leftMaxHeap)
            heapq.heappush(rightMinHeap, tmp)
            leftCnt -= 1
            rightCnt += 1
        elif rightCnt > leftCnt:
            tmp = heapq.heappop(rightMinHeap)
            heapq.heappush(leftMaxHeap, -tmp)
            rightCnt -= 1
            leftCnt += 1
        print(-leftMaxHeap[0])

