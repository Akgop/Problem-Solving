def solution(lines):
    answer = 0

    start = []
    end = []
    # preprocessing
    for i in range(len(lines)):
        _, s, t = lines[i].split()
        hour, minute, tmp = s.split(":")
        sec, milli = tmp.split(".")
        end_time = int(hour)*60*60*1000 + int(minute)*60*1000 + int(sec)*1000 + int(milli)
        start_time = end_time - int(float(t[:-1])*1000) + 1
        end.append(end_time)
        start.append(start_time)

    start.sort(reverse=True)
    end.sort(reverse=True)
    # 투 포인터
    count = 0
    while start:
        head = start[-1]
        count += 1
        start.pop()
        tail = head - 999
        while end[-1] < tail:
            count -= 1
            end.pop()
        answer = max(answer, count)

    return answer


print(solution([
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s"]
))

print(solution([
    "2016-09-15 01:00:04.002 2.0s",
    "2016-09-15 01:00:07.000 2s"
]))
