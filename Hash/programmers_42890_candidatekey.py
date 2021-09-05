from itertools import combinations


def solution(relation):
    col, row = len(relation[0]), len(relation)

    index = set(i for i in range(col))
    max_candidate_key = []

    for c in range(1, col + 1):
        for comb in combinations(list(index), c):       # 개수 만큼 뽑는다.
            tmp = set()
            for rel in relation:
                row = tuple(rel[c] for c in comb)       # 해당 열의 인덱스에 해당하는 값을 튜플로 임시 생성한다.
                if row in tmp:                          # 해당 값이 "유일(uniqueness)"하지 않다면
                    break
                tmp.add(row)
            else:
                for key in max_candidate_key:           # 앞선 단계에서 등록된 후보키를 순회하며
                    if set(key).issubset(set(comb)):    # 해당 후보키가 최소성을 만족하는지 체크
                        break
                else:
                    max_candidate_key.append(comb)

    return len(max_candidate_key)
