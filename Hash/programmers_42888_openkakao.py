def solution(record):
    result = []
    parsed = []
    uid_nick = dict()
    for r in record:
        tmp = r.split()
        parsed.append([tmp[0], tmp[1]])
        if tmp[0] == "Enter" or tmp[0] == "Change":
            uid_nick[tmp[1]] = tmp[2]

    for cmd, uid in parsed:
        if cmd == "Enter":
            result.append(f"{uid_nick[uid]}님이 들어왔습니다.")
        elif cmd == "Leave":
            result.append(f"{uid_nick[uid]}님이 나갔습니다.")

    return result


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))