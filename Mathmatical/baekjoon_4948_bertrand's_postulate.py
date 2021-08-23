import sys


def dp():
    flag = [True] * (MAX + 1)
    for i in range(2, int(MAX**0.5) + 1):
        if flag[i]:
            for j in range(2*i, MAX+1, i):
                flag[j] = False
    return flag


if __name__ == "__main__":
    MAX = 123456 * 2
    Table = dp()
    while True:
        N = int(sys.stdin.readline().rstrip())
        if N == 0:
            break
        cnt = 0
        for idx in range(N+1, 2*N+1):
            if Table[idx]:
                cnt += 1
        print(cnt)
