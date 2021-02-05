def get_coord(keypad, num):
    r = 0
    c = 0
    for i in range(4):
        if num in keypad[i]:
            r = i
            c = keypad[r].index(num)
    return r, c


def get_manhattan_distance(r, c, tar_r, tar_c):
    return abs(r-tar_r) + abs(c-tar_c)


def solution(numbers, hand):
    answer = ''

    # 별과 샾은 -1, -2로 초기화, 시작 위치 설정
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [-1, 0, -2]]
    left_hand = -1
    right_hand = -2
    
    # 문자열 시작
    for number in numbers:
        # 왼손인 경우
        if number == 1 or number == 4 or number == 7:
            answer += 'L'
            left_hand = number
        # 오른손인 경우
        elif number == 3 or number == 6 or number == 9:
            answer += 'R'
            right_hand = number
        # 경합 경우
        else:
            left_r, left_c = get_coord(keypad, left_hand)
            right_r, right_c = get_coord(keypad, right_hand)
            tar_r, tar_c = get_coord(keypad, number)
            left_dist = get_manhattan_distance(left_r, left_c, tar_r, tar_c)
            right_dist = get_manhattan_distance(right_r, right_c, tar_r, tar_c)
            # 왼손이 더 가까우면
            if left_dist < right_dist:
                answer += 'L'
                left_hand = number
            # 오른손이 더 가까우면
            elif right_dist < left_dist:
                answer += 'R'
                right_hand = number
            # 양손이 같으면
            elif hand == "right":
                answer += 'R'
                right_hand = number
            else:
                answer += 'L'
                left_hand = number

    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
