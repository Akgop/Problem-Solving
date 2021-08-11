def down(array, x, y, step, value):
    for i in range(step):
        array[x][y] = value
        x += 1
        value += 1
    return array, x - 1, y + 1, value


def right(array, x, y, step, value):
    for i in range(step):
        array[x][y] = value
        y += 1
        value += 1
    return array, x - 1, y - 2, value


def diagonal(array, x, y, step, value):
    for i in range(step):
        array[x][y] = value
        x -= 1
        y -= 1
        value += 1
    return array, x + 2, y + 1, value


def solution(n):
    answer = [[0]*n for _ in range(n)]
    MAX_VALUE = n*(n+1) // 2
    value = 1
    x, y = 0, 0
    step = n
    while True:
        answer, x, y, value = down(answer, x, y, step, value)
        if value > MAX_VALUE:
            break
        step -= 1
        answer, x, y, value = right(answer, x, y, step, value)
        if value > MAX_VALUE:
            break
        step -= 1
        answer, x, y, value = diagonal(answer, x, y, step, value)
        if value > MAX_VALUE:
            break
        step -= 1
    result = []
    for i in range(n):
        for j in range(i+1):
            result.append(answer[i][j])
    return result

print(solution(10))