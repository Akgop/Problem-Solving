def solution(participant, completion):
    answer = ''
    hash_table_p = dict()
    for p in participant:
        if p in hash_table_p:
            hash_table_p[p] += 1
        else:
            hash_table_p[p] = 1
    for c in completion:
        if c in hash_table_p:
            hash_table_p[c] -= 1
            if hash_table_p[c] == 0:
                hash_table_p.pop(c)
    answer = list(hash_table_p.keys())
    return answer[0]


print(solution(
    ["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]
))
