import sys
import copy


def solution(n):
    result = list()

    # 1~N 까지 내림차순 정렬
    desc = list()
    for i in range(n, 0, -1):
        desc.append(i)

    # stack 이용해서 수열 판별
    stack = list()
    stack.append(desc.pop())
    result.append('+')
    flag = True

    idx = 0
    while stack:
        if stack[len(stack) - 1] > seq[idx]:
            flag = False
            break
        # 타겟 찾았으면
        if stack[len(stack) - 1] == seq[idx]:
            stack.pop()
            result.append('-')
            idx += 1
            if not stack and desc:
                stack.append(desc.pop())
                result.append('+')
        else:
            stack.append(desc.pop())
            result.append('+')

    if not flag:
        print('NO')
        return

    for r in result:
        print(r)


# 다른 사람 코드인데 너무 잘짜서 가져왔음
# def solution():
#     stack, result, cnt = [], [], 1
#     for i in p:
#         while cnt <= i:
#             stack.append(cnt)
#             result.append('+')
#             cnt += 1
#         if stack.pop() != i:
#             return 'NO'
#         else:
#             result.append('-')
#     return '\n'.join(result)


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    seq = list()
    for _ in range(N):
        seq.append(int(sys.stdin.readline().rstrip()))
    solution(N)
