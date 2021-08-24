import sys


def check(summation, array):
    cur = summation
    row = len(array) - 1
    for i in range(len(index[row])):
        if index[row][i] == "+" and cur <= 0:
            return False
        if index[row][i] == "-" and cur >= 0:
            return False
        if index[row][i] == "0" and cur != 0:
            return False
        cur -= array[i]
    return True


def backtrack(answer, depth, max_depth, summation):
    if not check(summation, answer):
        return False

    if depth == max_depth-1:
        print(*answer)
        return True

    for value in numbers:
        answer.append(value)
        summation += value
        if backtrack(answer, depth+1, max_depth, summation):
            return True
        summation -= value
        answer.pop()
    return False


def solution(n):
    answer = []
    summation = 0
    for value in numbers:
        answer.append(value)
        summation += value
        if backtrack(answer, 0, n, summation):
            return True
        summation -= value
        answer.pop()


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    seq = list(sys.stdin.readline().rstrip())
    numbers = [Num for Num in range(-10, 11)]
    index = [[] for _ in range(N)]
    idx = 0
    for i in range(N):
        for j in range(i, N):
            index[j].append(seq[idx])
            idx += 1
    solution(N)

