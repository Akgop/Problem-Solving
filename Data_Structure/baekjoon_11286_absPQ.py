import sys
import heapq


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    array = []
    for _ in range(N):
        X = int(sys.stdin.readline().rstrip())
        if X:
            heapq.heappush(array, (abs(X), X))
        else:
            if array:
                print(heapq.heappop(array)[1])
            else:
                print(0)

