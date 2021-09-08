import heapq


def bfs(n, number):
    hq = []
    visited = set()
    depth = 1
    n_list = [int(str(n)*i) for i in range(1, 9)]
    for val in n_list:
        heapq.heappush(hq, (depth, val))
        visited.add(val)
        depth += 1
    while hq:
        depth, value = heapq.heappop(hq)

        if value == number:
            return depth
        if depth > 8:
            break

        for i in range(len(n_list) - depth):
            new_val = list()
            new_val.append(value + n_list[i])
            new_val.append(value - n_list[i])
            new_val.append(n_list[i] - value)
            new_val.append(n_list[i] * value)
            new_val.append(value // n_list[i])
            if value:
                new_val.append(n_list[i] // value)
            for val in new_val:
                if val not in visited:
                    visited.add(val)
                    heapq.heappush(hq, (depth + i + 1, val))

    return -1


def solution(N, number):
    return bfs(N, number)


print(solution(5, 12))
print(solution(2, 11))