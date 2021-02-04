def get_manhattan_distance(keypad, num, coord):
    num_r = 0
    num_c = 1
    for i in range(4):
        if num in keypad[i]:
            num_r = i
            break
    return abs(coord[0]-num_c) + abs(coord[1]-num_r)


def solution(numbers, hand):
    answer = ''

    # 별과 샾은 -1, -2로 초기화, 시작 위치 설정
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [-1, 0, -2]]
    left_hand = [3, 0]
    right_hand = [3, 2]
    
    # 문자열 시작
    for number in numbers:
        # 왼손인 경우
        if number == 1 or number == 4 or number == 7:
            answer += 'L'
            left_hand = [number // 3, 0]  # 왼손 위치 이동
        # 오른손인 경우
        elif number == 3 or number == 6 or number == 9:
            answer += 'R'
            right_hand = [(number // 3) - 1, 2]  # 오른손 위치 이동
        # 경합 경우
        else:
            left_dist = get_manhattan_distance(keypad, number, left_hand)
            right_dist = get_manhattan_distance(keypad, number, right_hand)
            # 왼쪽이 더 가까울 경우
            if left_dist < right_dist:
                answer += 'L'
                if number == 0:
                    left_hand = [3, 1]
                else:
                    left_hand = [number // 3, 1]
            # 오른쪽이 더 가까울 경우
            elif right_dist < left_dist:
                answer += 'R'
                if number == 0:
                    right_hand = [3, 1]
                else:
                    right_hand = [number // 3, 1]
            # 거리가 같은 경우
            else:
                if hand == "right":
                    answer += 'R'
                    if number == 0:
                        right_hand = [3, 1]
                    else:
                        right_hand = [number // 3, 1]
                else:
                    answer += 'L'
                    if number == 0:
                        left_hand = [3, 1]
                    else:
                        left_hand = [number // 3, 1]

                

    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
