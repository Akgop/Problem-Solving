import sys


def count_c(mid, n):
    prev = houses[0]
    count = 1
    for h in range(1, n):
        if houses[h] >= prev + mid:
            count += 1
            prev = houses[h]
    return count


def binary_search(start, end, c, n):
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        if count_c(mid, n) >= c:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1
    print(answer)


if __name__ == "__main__":
    N, C = map(int, sys.stdin.readline().rstrip().split())
    houses = list()
    for i in range(N):
        houses.append(int(sys.stdin.readline().rstrip()))
    houses.sort()
    binary_search(0, max(houses), C, N)


