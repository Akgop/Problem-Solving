def query_token(query, flag):
    idx = 0
    for i in range(len(query)):
        if query[i] == "?" and flag:
            idx = i
            break
        if query[i] != "?" and not flag:
            idx = i
            break
    if flag:
        return query[:idx], idx
    else:
        tmp = query[idx:]
        return tmp[::-1], len(query) - idx


def my_bisect_left(li, query, flag):
    # 쿼리 가공
    n = len(query)
    target, idx = query_token(query, flag)
    # 시작과 끝
    answer = -1
    start, end = 0, len(li) - 1
    while start <= end:
        mid = (start + end) // 2
        if len(li[mid]) < n:
            start = mid + 1
        elif len(li[mid]) > n:
            end = mid - 1
        else:
            if li[mid][:idx] >= target:
                end = mid - 1
                answer = mid
            else:
                start = mid + 1
    return answer


def my_bisect_right(li, query, flag):
    # 쿼리 가공
    n = len(query)
    target, idx = query_token(query, flag)
    # 시작과 끝
    answer = -1
    start, end = 0, len(li) - 1
    while start <= end:
        mid = (start + end) // 2
        if len(li[mid]) < n:
            start = mid + 1
        elif len(li[mid]) > n:
            end = mid - 1
        else:
            if li[mid][:idx] <= target:
                start = mid + 1
                answer = mid
            else:
                end = mid - 1
    return answer


def solution(words, queries):
    answer = []
    # 0. 와일드 카드가 앞에 있는 경우를 대비해 words 역순으로 구성
    reverse_words = []
    for word in words:      # O(100만) -> 전체 단어 길이의 합은 100만이기 때문
        reverse_words.append(word[::-1])

    # 1. words 를 sorting 한다. -> parametric search 를 하기 위해
    words.sort(key=lambda x: (len(x), x))
    reverse_words.sort(key=lambda x: (len(x), x))

    # 2. queries 를 하나씩 보며 words 를 이진 탐색
    for query in queries:
        # 와일드 카드가 앞에서 시작하는지, 뒤에어 시작하는지.
        left, right = 0, 0
        if query[-1] == "?":
            left = my_bisect_left(words, query, True)
            right = my_bisect_right(words, query, True)
        elif query[0] == "?":
            left = my_bisect_left(reverse_words, query, False)
            right = my_bisect_right(reverse_words, query, False)
        # 만약 찾는 값이 없으면
        if left == -1 or right == -1:
            answer.append(0)
        else:
            answer.append(right - left + 1)
    return answer


print(solution(
    ["frodo", "front", "frost", "frozen", "frame", "kakao", "a"],
    #["fro??", "????o", "fr???", "fro???", "pro?", "?????", "k????", "???zen"]
    ["?", "??", "???", "????", "?????", "??????"]
))