# update flag_list
def prime_number(m):
    for i in range(2, m+1):
        if flag_list[i] is True:
            for j in range(i, m+1, i):
                if i == j:
                    continue
                flag_list[j] = False


# Goldbach
def goldbach_partition(num):
    small = num // 2
    big = num // 2
    if small % 2 == 0:
        small -= 1
        big += 1
    while True:
        if flag_list[small] is True:
            if flag_list[big] is True:
                break
        small -= 2
        big += 2
    if num == 4:
        small = 2
        big = 2
    print(small, big)


case_list = []
t = int(input())
for _ in range(t):
    n = int(input())
    case_list.append(n)
maximum = max(case_list)
flag_list = [True] * (maximum+1)
prime_number(maximum)
for even in case_list:
    goldbach_partition(even)
