def solution():
    money.sort()

    target = 1
    for m in money:
        if target < m:
            break
        target += m
    return target


if __name__ == "__main__":
    money = [1, 2, 4]
    print(solution())
