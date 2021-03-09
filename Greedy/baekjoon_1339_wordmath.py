import sys


def solution(words):
    answer = 0
    words_math = dict()
    for word in words:  # 최대 10개
        wn = len(word)
        for i in range(wn-1, -1, -1):  # 최대 8개
            if word[i] in words_math:   # O(1)
                words_math[word[i]] += 10**(wn - 1 - i)
            else:
                words_math[word[i]] = 10**(wn - 1 - i)

    words_math_list = list(words_math.items())
    words_math_list.sort(key=lambda x: x[1], reverse=True)

    cnt = 9
    for word_tuple in words_math_list:
        words_math[word_tuple[0]] = cnt
        cnt -= 1

    for word in words:
        tmp = 0
        wn = len(word)
        for i in range(wn-1, -1, -1):
            tmp += words_math[word[i]]*10**(wn-1-i)
        answer += tmp
    return answer


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    _words = list()
    for _ in range(N):
        _words.append(list(sys.stdin.readline().rstrip()))
    print(solution(_words))
