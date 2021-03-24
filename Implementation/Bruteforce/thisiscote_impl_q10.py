def rotate_right(key):
    key = list(zip(*key[::-1]))
    return key


def get_sum(lock, n, m):
    answer = 0
    for i in range(n):
        for j in range(n):
            if lock[i+m-1][j+m-1] == 1:
                answer += 1
    return answer


def cal_two(lock, key, r, c, m, f):
    for i in range(m):
        for j in range(m):
            if f:
                lock[i+r][j+c] += key[i][j]
            else:
                lock[i+r][j+c] -= key[i][j]
    return lock


def solution(key, lock):
    n = len(lock)
    m = len(key)

    # key 의 크기만큼 resize
    new_size = 2 * m + n - 2
    resized_lock = [[0] * new_size for _ in range(new_size)]
    for i in range(n):
        for j in range(n):
            resized_lock[i+m-1][j+m-1] = lock[i][j]
    expected = n ** 2
    
    # 4 방향 회전하며 구함
    for _ in range(4):
        # 2D list 순차 탐색
        for i in range(new_size - m + 1):
            for j in range(new_size - m + 1):
                resized_lock = cal_two(resized_lock, key, i, j, m, True)
                tmp = get_sum(resized_lock, n, m)
                if tmp == expected:
                    return True
                resized_lock = cal_two(resized_lock, key, i, j, m, False)
        key = rotate_right(key)
    return False


print(
    solution(
        [[0, 0, 0],
         [1, 0, 0],
         [0, 1, 1]],
        [[1, 1, 1],
         [1, 1, 0],
         [1, 0, 1]]
    )
)
