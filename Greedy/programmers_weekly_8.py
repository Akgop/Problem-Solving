# 그리디
def solution(sizes):
    garo, sero = 0, 0
    # 1. sizes 순회하며 가로 세로 값 업데이트
    for row, col in sizes:
        # 2. row, col을 그대로 쓰는게 이득인 경우
        size_o = max(garo, row) * max(sero, col)
        size_t = max(garo, col) * max(sero, row)
        if size_o <= size_t:
            garo = row if row > garo else garo
            sero = col if col > sero else sero
        else:
            garo = col if col > garo else garo
            sero = row if row > sero else sero

    return garo * sero