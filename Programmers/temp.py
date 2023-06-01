class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.pre = None


def printNodes(node: Node):
    crnt_node = node
    res = []
    while crnt_node is not None:
        res.append(crnt_node.val)
        crnt_node = crnt_node.next
    return res


class LinkedList:
    def __init__(self):
        self.head = None

    def move(self, node, val):  # O(1)
        crnt_node = node
        if val < 0:
            for _ in range(abs(val)):
                crnt_node = crnt_node.pre
        else:
            for _ in range(abs(val)):
                crnt_node = crnt_node.next
        return crnt_node

    def addAtHead(self, val):  # O(1)
        node = Node(val)
        node.next = self.head
        node.pre = None
        self.head = node

    # but when the list
    def addBack(self, val):  # O(n)
        node = Node(val)
        crnt_node = self.head
        while crnt_node.next:
            crnt_node = crnt_node.next
        crnt_node.next = node
        crnt_node.next.pre = crnt_node

    def findNode(self, val):  # O(n)
        crnt_node = self.head
        while crnt_node is not None:
            if crnt_node.val == val:
                return crnt_node
            crnt_node = crnt_node.next
        raise RuntimeError("Node not found")

    def addAfter(self, node, new_node):  # O(1)
        if node.next != None:
            new_node.next = node.next.next
        else:
            new_node.next = node.next
        new_node.pre = node.pre
        node.next = new_node

    def delete(self, node):  # O(1)
        crnt_node = node.pre
        crnt_node.next = node.next
        if node.next == None:
            pass
        else:
            crnt_node = node.next
            crnt_node.pre = node.pre
        return crnt_node


def solution(n, k, cmds):
    answer = ""
    deleted = []

    root = LinkedList()
    root.addAtHead(0)
    for i in range(1, n):
        root.addBack(i)
    curr = root.findNode(k)
    for cmd in cmds:
        cmd = cmd.split(" ")
        if cmd[0] == "U":
            curr = root.move(curr, -int(cmd[1]))
        elif cmd[0] == "D":
            curr = root.move(curr, int(cmd[1]))
        elif cmd[0] == "C":
            deleted.append(curr)
            curr = root.delete(curr)
        else:
            temp = deleted.pop()
            root.addAfter(temp.pre, temp)

    print(printNodes(root.head))
    pre = 0
    for i in printNodes(root.head):
        temp = i - pre
        if temp == 1:
            answer = answer + "O"
        elif temp == 0:
            answer = answer + "O"
        else:
            for _ in range(temp - 1):
                answer = answer + "X"
        pre = i
    if len(answer) != n:
        for _ in range(n - len(answer)):
            answer = answer + "O"
    print(answer)
    return answer


solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"])
solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"])
