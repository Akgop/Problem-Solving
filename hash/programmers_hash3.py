def solution(clothes):
    answer = 1
    categories = dict()
    for cloth in clothes:
        if cloth[1] in categories:
            categories[cloth[1]] += 1
        else:
            categories[cloth[1]] = 2
    value_list = list(categories.values())
    for cnt in value_list:
        answer *= cnt
    answer -= 1
    return answer


print(
    solution(
        [["yellow_hat", "headgear"],
         ["blue_sunglasses", "eyewear"],
         ["green_turban", "headgear"],
         ["crow_mask", "face"]]
    )
)
