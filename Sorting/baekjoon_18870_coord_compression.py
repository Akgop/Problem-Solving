import sys


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    li = list(map(int, sys.stdin.readline().rstrip().split()))
    sorted_li = list(sorted(set(li)))
    dic = {sorted_li[i]: i for i in range(len(sorted_li))}
    for i in range(N):
        print(dic[li[i]], end=' ')
