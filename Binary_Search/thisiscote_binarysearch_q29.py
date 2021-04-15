import sys


def count_c(n, step):
    prev = houses[0]
    count = 1
    for i in range(1, n):
        # 이전 노드와 step 만큼 차이가 나는가?
        if houses[i] >= prev + step:
            count += 1
            prev = houses[i]
    return count


def binary_search(n, c):
    start = 0
    end = houses[-1]
    answer = 0
    while start <= end:
        # mid 의 의미는 몇 칸씩 집을 띄어서 공유기를 설치할 지
        mid = (start + end) // 2
        if count_c(n, mid) >= c:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    return answer


if __name__ == "__main__":
    N, C = map(int, sys.stdin.readline().rstrip().split())
    houses = []
    for _ in range(N):
        houses.append(int(sys.stdin.readline().rstrip()))
    houses.sort()
    print(binary_search(N, C))
