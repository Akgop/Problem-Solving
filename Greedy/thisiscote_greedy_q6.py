def solution(food_times, k):
    n = len(food_times)
    plate = n       # 남은 접시

    overflow = k
    for f in food_times:
        overflow -= f
    if overflow >= 0:
        return -1

    while True:
        quo = k // plate        # 남은 접시 row 구함
        remain = k % plate      # 남은 접시 col 구함

        # 접시 하나 남았으면 그게 답
        if plate == 1:
            for i in range(n):
                if food_times[i] != 0:
                    return i + 1

        # 먹어야할 접시가 남은 경우 먹는다.
        tmp_remain = remain + (quo * plate)
        empty = 0
        for i in range(n):
            if food_times[i] < quo:
                empty += quo - food_times[i]
                food_times[i] = 0
            else:
                food_times[i] -= quo
            # 만약 먹다가 나머지가 끝나버린다 -> 종료
            if tmp_remain == 0:
                return i + 1
            if food_times[i] != 0:
                tmp_remain -= 1

        tmp_plate = n
        for f in food_times:
            if f == 0:
                tmp_plate -= 1

        k = empty + remain
        plate = tmp_plate


print(
    solution(
        [4, 1, 3],
        4
    )
)
