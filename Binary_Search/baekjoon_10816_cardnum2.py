import sys


def solution():
    cards_dict = dict()
    for card in cards:
        if card in cards_dict:
            cards_dict[card] += 1
        else:
            cards_dict[card] = 1

    for target in targets:
        if target in cards_dict:
            print(cards_dict[target], end=' ')
        else:
            print(0, end=' ')


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    cards = list(map(int, sys.stdin.readline().rstrip().split()))
    M = int(sys.stdin.readline().rstrip())
    targets = list(map(int, sys.stdin.readline().rstrip().split()))
    solution()
