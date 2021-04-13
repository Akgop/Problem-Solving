def solution(n, li):
    answer = -1
    left, right = 0, len(li)-1
    while left <= right:
        mid = (left + right) // 2
        if li[mid] == mid:
            answer = mid
            break
        elif li[mid] < mid:
            left = mid + 1
        else:
            right = mid - 1
    return answer


print(solution(
    5, [-15, -6, 1, 3, 7]
))

print(solution(
    7, [-15, -4, 2, 8, 9, 13, 15]
))

print(solution(
    7, [-15, -4, 3, 8, 9, 13, 15]
))