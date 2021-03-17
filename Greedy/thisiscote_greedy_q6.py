def get_sum(li, n, mid):
    answer = 0
    for i in range(n):
        if li[i] < mid:
            answer += li[i]
        else:
            answer += mid
    return answer


def binary_search(li, k, start, end, n):
    answer = 0
    result_food_ate = 0
    while start <= end:
        mid = (start + end) // 2
        food_ate = get_sum(li, n, mid)
        if food_ate > k:
            end = mid - 1
        else:
            answer = mid
            result_food_ate = food_ate
            start = mid + 1
    return answer, result_food_ate


def solution(food_times, k):
    n = len(food_times)
    answer, food_ate = binary_search(food_times, k, 0, max(food_times), n)

    idx = k - (food_ate - 1)
    print(k, food_ate, idx, answer)
    for i in range(n):
        if food_times[i] <= answer:
            continue
        idx -= 1
        if idx == 0:
            return i + 1
    return -1


print(
    solution(
        [4, 2, 3, 6, 7, 1, 5, 8],
        16
    )
)
# food_times=[4,2,3,6,7,1,5,8] k=16 answer = 3
# food_times=[4,2,3,6,7,1,5,8] k=27 answer = 5
