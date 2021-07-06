import sys

# 다른 사람이 짠 dp 코드. 엄청 깔끔한데 어떻게 이런 생각을 할 수 있을지 잘 모르겠다..
# def solution(n):
#     a, b, c = 0, 0, 0
#     for w in wine:
#         a, b, c = max(a, b, c), a + w, b + w
#     return max(a, b, c)


def solution(n):
    if n < 3:
        return sum(wine)
    result = [0] * n
    result[0] = wine[0]
    result[1] = wine[0] + wine[1]
    result[2] = max(wine[0] + wine[1], wine[0] + wine[2], wine[1] + wine[2])
    for i in range(3, n):
        result[i] = max(
            result[i-3] + wine[i-1] + wine[i],
            result[i-2] + wine[i],
            result[i-1]
        )
    return result[-1]


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    wine = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
    print(solution(N))
