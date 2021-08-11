import heapq


def solution(jobs):
    jobs.sort(reverse=True)
    job_cnt = len(jobs)
    cur_time = 0
    heap = []
    # 시작 시간 초기화
    answer = 0
    while True:
        # 시간에 맞게 들어오는 요청을 모두 heap 에 넣는다.
        while True:
            if jobs and jobs[-1][0] <= cur_time:
                req_time, runtime = jobs.pop()
                heapq.heappush(heap, (runtime, req_time))
                continue
            break
        # 반복문 탈출 조건
        if not heap:
            if not jobs:
                break
            cur_time += 1
            continue
        # heap 에서 원소 하나 빼서 일을 진행한다
        runtime, req_time = heapq.heappop(heap)
        cur_time += runtime
        answer += (cur_time - req_time)
    return answer // job_cnt


print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[1, 3], [2, 3]]))
print(solution([[8, 3], [0, 10], [0, 14]]))
