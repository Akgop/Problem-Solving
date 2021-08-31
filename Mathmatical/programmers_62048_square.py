from math import gcd, ceil, floor


def calculate(qw, slope):
    count = int(ceil(slope))
    cur = slope
    for i in range(1, qw-1):
        count += int(ceil(cur + slope)) - int(floor(cur))
        cur += slope
    if qw > 1:
        count += int(ceil(slope))
    return count


def solution(w, h):
    if w > h:
        w, h = h, w
    quote = gcd(w, h)
    qw = w // quote
    qh = h // quote
    slope = qh / qw
    print(slope)
    return w*h - calculate(qw, slope)*quote
