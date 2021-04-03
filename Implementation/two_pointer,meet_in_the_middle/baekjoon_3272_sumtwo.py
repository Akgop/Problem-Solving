import sys


def solution(n, x):
    # 두 포인터 생성
    front, back = 0, n-1

    # 앞이 뒤를 넘어설 때 까지
    answer = 0
    while front < back:
        tmp = li[front] + li[back]
        # 두 합이 더 크면
        if tmp > x:
            back -= 1
        # 두 합이 같다면
        elif tmp == x:
            answer += 1
            front += 1
        # 두 합이 더 작으면
        else:
            front += 1
    print(answer)


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    li = list(map(int, sys.stdin.readline().rstrip().split()))
    X = int(sys.stdin.readline().rstrip())
    li.sort()
    solution(N, X)
