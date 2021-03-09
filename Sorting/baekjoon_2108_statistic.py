import sys


def arithmetic_mean(l):
    s = sum(l)
    t = len(l)
    temp = s/t
    result = s//t
    if temp - result >= 0.5:
        result = result + 1
    return result


def median(l):
    l.sort()
    return l[len(l)//2]


def mode(c):
    val = -1
    result = 0
    flag = 0
    res = sorted(c.items())
    for e in res:
        if e[1] > val:
            result = e[0]
            val = e[1]
            flag = 0
        elif e[1] == val:
            if flag != 0:
                continue
            else:
                result = e[0]
                flag += 1
    return result


N = int(input())
li = []
count = {}
for _ in range(N):
    num = int(sys.stdin.readline())
    li.append(num)
    if num in count:
        count[num] = count[num] + 1
    else:
        count[num] = 1

print(arithmetic_mean(li))
print(median(li))
print(mode(count))
print(max(li)-min(li))


