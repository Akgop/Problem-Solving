import sys


def solution(n):
    # 입력의 최댓값 만큼 메모리 할당
    table = [0] * 1001

    table[0] = 1
    table[1] = 3
    for i in range(2, n):
        table[i] = (table[i-1] + 2*table[i-2]) % 796796
    return table[n-1]


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    print(solution(N))
