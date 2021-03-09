import sys


def solution(lst):
    lst.sort(reverse=True)
    answer = ' '.join(lst)
    return answer


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    li = list()
    for _ in range(N):
        li.append(sys.stdin.readline().rstrip())
    print(solution(li))
