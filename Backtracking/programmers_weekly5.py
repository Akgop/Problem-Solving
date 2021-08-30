def backtrack(string, target, depth, max_depth, count, alpha):
    global answer
    answer += 1
    if string == target:
        return True
    if depth == max_depth:
        return False
    for i in range(5):
        if count[i] == 0:
            continue
        count[i] -= 1
        if backtrack(string + alpha[i], target, depth+1, max_depth, count, alpha):
            return True
        count[i] += 1
    return False


def solution(word):
    global answer
    count = [5, 5, 5, 5, 5]
    alpha = ['A', 'E', 'I', 'O', 'U']
    for i in range(5):
        count[i] -= 1
        if backtrack(alpha[i], word, 1, 5, count, alpha):
            break
        count[i] += 1
    return answer


answer = 0