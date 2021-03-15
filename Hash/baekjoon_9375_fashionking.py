import sys


def solution(n):
    answer = 1
    for k, v in clothes.items():
        answer *= (v+1)
    return answer - 1


if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        N = int(sys.stdin.readline().rstrip())
        clothes = dict()
        for _ in range(N):
            _, key = map(str, sys.stdin.readline().rstrip().split())
            try:
                clothes[key] += 1
            except:
                clothes[key] = 1
        print(solution(N))
