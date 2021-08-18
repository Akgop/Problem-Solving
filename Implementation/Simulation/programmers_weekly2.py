def grade(answer, num):
    if num >= 90:
        return answer + 'A'
    if num >= 80:
        return answer + 'B'
    if num >= 70:
        return answer + 'C'
    if num >= 50:
        return answer + 'D'
    else:
        return answer + 'F'


def solution(scores):
    answer = ''
    for col in range(len(scores)):
        row_max = scores[col][col]
        row_min = scores[col][col]
        tmp = []
        dup = False
        for row in range(len(scores)):
            if row == col:
                continue
            if scores[row][col] > row_max:
                row_max = scores[row][col]
            if scores[row][col] < row_min:
                row_min = scores[row][col]
            if scores[row][col] == scores[col][col]:
                dup = True
            tmp.append(scores[row][col])
        if (row_max == scores[col][col] or row_min == scores[col][col]) and not dup:
            result = sum(tmp) / (len(scores)-1)
            answer = grade(answer, result)
            continue
        result = (sum(tmp) + scores[col][col]) / len(scores)
        answer = grade(answer, result)

    return answer


print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))
