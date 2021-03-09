import sys


def solution(n, li):
    if len(li) == 1:
        return -1
    li.sort()
    odd_li = li[0::2]
    even_li = li[1::-2]
    even_li.reverse()
    new_li = odd_li + even_li
    _max = abs(new_li[1] - new_li[0])
    for i in range(1, len(new_li)-1):
        tmp = abs(new_li[i+1] - new_li[i])
        if tmp > _max:
            _max = tmp
    return _max


if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        N = int(sys.stdin.readline().rstrip())
        L = list(map(int, sys.stdin.readline().rstrip().split()))
        print(solution(N, L))
