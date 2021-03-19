import sys


alpha = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
         'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
         'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
number = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}


def solution(n):
    letters = []
    nums = []
    for s in S:
        if s in alpha:
            letters.append(s)
        if s in number:
            nums.append(int(s))
    letters.sort()
    answer = ''.join(letters)
    print(answer, end='')
    if len(nums) != 0:
        print(sum(nums))


if __name__ == "__main__":
    S = list(sys.stdin.readline().rstrip())
    solution(len(S))
