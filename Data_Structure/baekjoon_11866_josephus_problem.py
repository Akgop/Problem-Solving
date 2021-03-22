import sys
from collections import deque


def solution(n, k):
    # 초기 설정
    q = deque()
    for i in range(1, n+1):
        q.append(i)

    answer = '<'
    # 원형 리스트를 돌며 popleft, append
    while q:
        # k - 1 번 popleft -> append
        for _ in range(k-1):
            now = q.popleft()
            q.append(now)
        
        # k 번째 popleft 후 출력
        now = q.popleft()
        answer += str(now) + ', '

    print(answer[:len(answer)-2] + ">")
    

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().rstrip().split())
    solution(N, K)
