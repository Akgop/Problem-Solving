import sys


def solution():
    heights.sort()
    total = sum(heights)
    for i in range(8):
        for j in range(i+1, 9):
            if total - heights[i] - heights[j] == 100:
                for m in range(9):
                    if m == i or m == j:
                        continue
                    print(heights[m])
                return


if __name__ == "__main__":
    heights = []
    for _ in range(9):
        heights.append(int(sys.stdin.readline().rstrip()))
    solution()
