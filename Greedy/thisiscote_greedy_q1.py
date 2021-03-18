import sys

"""
1번째 풀이 - 틀림
-> 조건을 전부 확인하지 않음. 몇 명의 모험가는 마을에 그대로 남아있어도 된다.
"""
# def solution(n):
#     li.sort(reverse=True)
#     count = 0
#     i = 0
#     while i < len(li):
#         i = i + li[i]
#         count += 1
#     print(count)


def solution(n):
    li.sort()
    count = 0
    group = 0
    for i in range(n):
        count += 1
        if li[i] <= count:
            count = 0
            group += 1
    print(group)


if __name__ == "__main__":
    li = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    N = len(li)
    solution(N)
