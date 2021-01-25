def solution(genres, plays):
    answer = []
    n = len(genres)
    table = dict()
    for i in range(n):
        if genres[i] in table:
            table[genres[i]][0][1] += plays[i]
            tmp_list = table[genres[i]]
            if len(tmp_list) < 3:
                tmp_list.append([i, plays[i]])
            else:
                if tmp_list[2][1] < plays[i]:
                    tmp_list[2][0] = i
                    tmp_list[2][1] = plays[i]
            tmp_list.sort(key=lambda x: x[1], reverse=True)
        else:
            table[genres[i]] = [[-1, plays[i]], [i, plays[i]]]
    value_list = list(table.values())
    value_list.sort(key=lambda x: x[0][1], reverse=True)
    for e in value_list:
        for i in range(1, len(e)):
            answer.append(e[i][0])
    return answer


print(
    solution(
        ["classic", "pop", "classic", "classic", "pop"],
        [500, 600, 150, 800, 2500]
    )
)
