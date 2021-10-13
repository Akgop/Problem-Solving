# import sys
#
#
# def preorder(node):
#     if node == '.':
#         return
#     print(node, end='')
#     preorder(tree[node][0])
#     preorder(tree[node][1])
#
#
# def inorder(node):
#     if node == '.':
#         return
#     inorder(tree[node][0])
#     print(node, end='')
#     inorder(tree[node][1])
#
#
# def postorder(node):
#     if node == '.':
#         return
#     postorder(tree[node][0])
#     postorder(tree[node][1])
#     print(node, end='')
#
#
# if __name__ == "__main__":
#     N = int(sys.stdin.readline().rstrip())
#     tree = dict()
#     for _ in range(N):
#         me, left, right = map(str, sys.stdin.readline().rstrip().split())
#         tree[me] = [left, right]
#     preorder('A')
#     print()
#     inorder('A')
#     print()
#     postorder('A')

import sys


def traversal(node):
    global pre, ino, pos
    if node == ".":
        return
    pre += node
    traversal(tree[node][0])
    ino += node
    traversal(tree[node][1])
    pos += node


if __name__ == "__main__":
    pre, ino, pos = "", "", ""
    N = int(sys.stdin.readline().rstrip())
    tree = dict()
    for _ in range(N):
        me, left, right = map(str, sys.stdin.readline().rstrip().split())
        tree[me] = [left, right]
    traversal('A')
    print(pre)
    print(ino)
    print(pos)
