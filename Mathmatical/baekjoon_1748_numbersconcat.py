def solution(n):
    n_str = list(str(n))
    answer = 0
    digit = '9'
    for i in range(len(n_str)-1, 0, -1):
        answer += (int(digit) * (len(n_str) - i))
        digit += '0'
    answer += (n - (10 ** (len(n_str) - 1) - 1)) * len(n_str)
    return answer


if __name__ == "__main__":
    N = int(input())
    print(solution(N))
