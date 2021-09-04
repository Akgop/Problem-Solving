from itertools import combinations


def solution(relation):
    col, row = len(relation[0]), len(relation)

    index = set(i for i in range(col))
    result = []

    for c in range(1, col + 1):
        for comb in combinations(list(index), c):
            tmp = set()
            for rel in relation:
                row = tuple(rel[c] for c in comb)
                if row in tmp:
                    break
                tmp.add(row)
            else:
                for key in result:
                    if set(key).issubset(set(comb)):
                        break
                else:
                    result.append(comb)

    return len(result)


print(solution([["100","ryan","music","2"],
                ["200","apeach","math","2"],
                ["300","tube","computer","3"],
                ["400","con","computer","4"],
                ["500","muzi","music","3"],
                ["600","apeach","music","2"]]
               ))
