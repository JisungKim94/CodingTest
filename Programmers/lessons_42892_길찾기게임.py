import sys

sys.setrecursionlimit(10**6)
# 기본 재귀 깊이 1000 제한 해제


class Node:
    def __init__(self, x, nodenum):
        self.node = nodenum
        self.x = x
        self.l = None
        self.r = None


def insert(n, x, nodenum):
    if n == None:
        return Node(x, nodenum)
    # 조건에 따라 l,r이 root 노드로 재귀
    if x < n.x:
        n.l = insert(n.l, x, nodenum)
    else:
        n.r = insert(n.r, x, nodenum)
    return n


def preorder(root):
    res = []

    def _preorder(node):
        if node:
            # 전위 순서
            res.append(node.node)
            _preorder(node.l)
            _preorder(node.r)

    _preorder(root)
    return res


def postorder(root):
    res = []

    def _postorder(node):
        if node:
            # 후위순서
            _postorder(node.l)
            _postorder(node.r)
            res.append(node.node)

    _postorder(root)
    return res


def solution(nodeinfo):
    answer = []
    for i, v in enumerate(nodeinfo):
        v.append(i + 1)
    nodeinfo.sort(key=lambda x: (-x[1], x[0]))

    # nodes를 순회하면서 이진 탐색 트리를 만든다.
    root = None
    for info in nodeinfo:
        root = insert(root, info[0], info[2])

    # print(root)
    answer.append(preorder(root))
    answer.append(postorder(root))
    # print(postorder(root))
    return answer


print(
    solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]])
    == [[7, 4, 6, 9, 1, 8, 5, 2, 3], [9, 6, 5, 8, 1, 4, 3, 2, 7]]
)
