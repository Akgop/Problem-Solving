from collections import Counter


def create_dict(string):
    tmp = []
    for i in range(len(string)-1):
        if not string[i].isalpha() or not string[i+1].isalpha():
            continue
        tmp.append(string[i:i+2])
    return Counter(tmp)


def get_lower(string):
    return string.lower()


def get_union_intersection(a_dict, b_dict):
    union, intersection = 0, 0
    for key, value in a_dict.items():
        if key in b_dict:               # a, b 둘 다 존재해
            intersection += min(a_dict[key], b_dict[key])
            union += max(a_dict[key], b_dict[key])
        else:
            union += a_dict[key]            # a 에만 존재해
    for key, value in b_dict.items():
        if key not in a_dict:               # b 에만 존재해
            union += b_dict[key]
    return union, intersection


def solution(str1, str2):
    a = get_lower(str1)
    b = get_lower(str2)
    a_dict = create_dict(a)
    b_dict = create_dict(b)
    union, intersection = get_union_intersection(a_dict, b_dict)
    if union == 0:
        answer = 1
    else:
        answer = intersection / union
    return int(answer * 65536)
