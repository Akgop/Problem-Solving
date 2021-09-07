def solution(weights, head2head):
    answer = []
    n = len(weights)
    result = []
    for i in range(n):
        win_cnt, win_cnt_heavier, total_game = 0, 0, 0
        for j in range(n):
            fight = head2head[i][j]
            if fight == 'N':
                continue
            if fight == 'L':
                total_game += 1
                continue
            if fight == 'W':
                if weights[i] < weights[j]:
                    win_cnt_heavier += 1
                win_cnt += 1
                total_game += 1
        win_rate = (win_cnt / total_game) if total_game != 0 else 0
        result.append([win_rate, win_cnt_heavier, weights[i], i+1])
    result.sort(key=lambda x: (-x[0], -x[1], -x[2], x[3]))
    for r in result:
        answer.append(r[3])
    return answer


print(solution([50,82,75,120], ["NLWL","WNLL","LWNW","WWLN"]))