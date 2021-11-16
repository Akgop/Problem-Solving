import sys


class Trie:
    def __init__(self):
        self.root = dict()

    def add(self, li):
        cur = self.root
        for e in li:
            if e not in cur:
                cur[e] = dict()
            cur = cur[e]
        cur[0] = True

    def travel(self, depth, cur):
        if 0 in cur:
            return

        keys = sorted(cur)

        for key in keys:
            print("--"*depth + key)
            self.travel(depth+1, cur[key])


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    trie = Trie()
    for _ in range(N):
        foods = list(map(str, sys.stdin.readline().split()))[1:]
        trie.add(foods)
    trie.travel(0, trie.root)
