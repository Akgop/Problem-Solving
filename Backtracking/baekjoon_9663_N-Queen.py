def n_queen(depth, n, answer):
    if depth == n:          # 마지막 행이라면 수행 완료
        return answer + 1   # +1 한 값을 return
    for i in range(n):      # n번 반복
        # 대각선 값의 visited 판별 각 1차원으로 보고 품
        if not V[i] and not D45[depth+i] and not D135[depth-i+n-1]:
            V[i] = True     # 행에 대해 판별
            D45[depth+i] = True     # y = -x 대각선 업데이트
            D135[depth-i+n-1] = True    # y = x 대각선 업데이트
            answer = n_queen(depth+1, n, answer)    # backtracking
            V[i] = False
            D45[depth + i] = False
            D135[depth - i + n - 1] = False
    return answer


N = int(input())
# 2차원 배열이 아닌 1차원 배열 3개로 판단
V, D45, D135 = [False]*N, [False]*(2*N-1), [False]*(2*N-1)
A = 0
A = n_queen(0, N, A)
print(A)

