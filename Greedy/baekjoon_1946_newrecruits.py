import sys


def solution(ranks, n):
    answer = 1
    # 한 종목을 오름차순으로 정렬
    ranks.sort(key=lambda x: x[0])  # O(NlogN)
    rank_min = ranks[0][1]
    # 나머지 한 종목을 순회하며 검사 O(N)
    for rank in ranks:
        if rank[1] < rank_min:
            rank_min = rank[1]
            answer += 1
    return answer


if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())
    # solution 제외 O(TN) -> 약 200만
    # solution O(NlogN) -> 약 50만
    # 도합 O(TNlogN) -> 약 1000만
    # 제한시간이 2초 이므로 약 2000만번의 수행 이내에 끝내야 한다.
    for _ in range(T):
        test_ranks = list()
        N = int(sys.stdin.readline().rstrip())
        for _ in range(N):
            doc, interview = map(int, sys.stdin.readline().rstrip().split())
            test_ranks.append([doc, interview])

        print(solution(test_ranks, N))
