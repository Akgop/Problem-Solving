from itertools import combinations


def check(relation, li, row):
    dup = set()
    for r in range(row):
        tmp = []
        for i in li:
            tmp.append(relation[r][i])
        tup_tmp = tuple(tmp)
        if tup_tmp in dup:
            return False
        dup.add(tup_tmp)
    return True


def solution(relation):
    answer = 0

    col = len(relation[0])
    row = len(relation)

    visited = [i for i in range(col)]
    for i in range(1, col + 1):
        combination = combinations(visited, i)
        for li in combination:
            if -1 in li:
                continue
            if check(relation, li, row):
                for v in li:
                    visited[v] = -1
                answer += 1
    return answer


print(solution([["100","ryan","music","2"],
                ["200","apeach","math","2"],
                ["300","tube","computer","3"],
                ["400","con","computer","4"],
                ["500","muzi","music","3"],
                ["600","apeach","music","2"]]
               ))
