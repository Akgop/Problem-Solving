def solution(s):
    # 문자열 길이 측정
    n = len(s)
    if n == 1:
        return 1
    result = list()
    # 길이만큼 Brute Force -> 길이가 1000밖에 안되서
    for unit in range(1, n//2 + 1):       # 자르는 단위 증가하며(반만 탐색해도됨)
        tmp_answer = ''
        count = 1                      # 구간 같은 개수 카운트
        last = ''
        for i in range(unit, n, unit):    # 문자열 순차 탐색
            prev = s[i-unit:i]         # 이전 구간의 문자열
            now = s[i:i+unit]          # 현재 구간
            if prev == now:     # 문자열이 반복되는 경우
                count += 1
            elif count < 2:     # 결과에 더할 때 숫자를 생략해야 하는 경우
                tmp_answer += prev
                count = 1
            else:               # 결과에 더할 때 숫자를 넣어야 하는 경우
                tmp_answer += str(count) + prev
                count = 1
            last = now
        # 마지막 범위인 경우
        if count < 2:
            tmp_answer += last
        else:
            tmp_answer += str(count) + last
        result.append((len(tmp_answer), tmp_answer))
    result.sort(key=lambda x: x[0])     # 얘도 길이가 아무리 커도 1000보다 작음
    answer = result[0]
    print(answer[0])
    return answer


solution(
    "a"
)
solution(
    "aabbaccc"
)
solution(
    "ababcdcdababcdcd"
)
solution(
    "abcabcdede"
)
solution(
    "abcabcabcabcdededededede"
)
solution(
    "xababcdcdababcdcd"
)