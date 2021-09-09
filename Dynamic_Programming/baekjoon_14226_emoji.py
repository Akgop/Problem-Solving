from collections import deque


def dp(target):
    que = deque()
    visited = set()
    que.append([0, 1, 0])   # 시간, 화면, 클립보드
    visited.add((1, 0))
    while que:
        time, screen, clipboard = que.popleft()
        if screen == target:
            return time

        # 화면 -> 클립보드 복사
        tup_list = list()
        tup_list.append((screen, screen))

        # 클립보드 -> 화면 붙여넣기
        if clipboard:
            tup_list.append((screen+clipboard, clipboard))

        # 화면에서 1개 삭제
        if screen:
            tup_list.append((screen-1, clipboard))

        for tup in tup_list:
            if tup not in visited:
                que.append([time+1, tup[0], tup[1]])
                visited.add(tup)
    return -1


def solution(s):
    return dp(s)


if __name__ == "__main__":
    print(solution(int(input())))