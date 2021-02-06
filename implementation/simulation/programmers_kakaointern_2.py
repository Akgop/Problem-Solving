def solution(gems):
    answer = []
    # in 메서드를 쓰기 위해 hash 구조로 저장
    gem_set = set()
    for gem in gems:
        gem_set.add(gem)
    # dict 자료구조로 현재 window 에 포함된 보석 개수 카운트
    gem_dict = dict()

    low, high = 0, 0
    for gem in gems:
        # gem 하나 넣고
        if gem in gem_dict:
            gem_dict[gem] += 1
        else:
            gem_dict[gem] = 1
        high += 1
        # 아직 모든 종류를 고르지 못했다면
        if len(gem_dict) < len(gem_set):
            continue
        # 모든 종류를 골랐다면 is_full == True
        # low 를 하나씩 당길 차례
        for i in range(low, high):
            # 앞의 gem 부터 뺀다.
            gem_dict[gems[i]] -= 1
            low += 1
            if gem_dict[gems[i]] == 0:
                if (high - low) < answer[2]:
                    answer = [low, high, high - low]
                gem_dict.pop(gems[i])
                break
    return answer[0:2]


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
