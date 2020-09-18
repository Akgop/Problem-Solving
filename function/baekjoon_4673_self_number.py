generators = set()


def generating_self_num(num):
    result = num
    for i in range(1, len(str(num))+1):
        result += num % 10
        num = num // 10
    return result


def iteration():
    for i in range(1, 10000):
        generators.add(generating_self_num(i))


def print_result():
    for i in range(1, 10000):
        if i in generators:
            pass
        else:
            print(i)


iteration()
print_result()
