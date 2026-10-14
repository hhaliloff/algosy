class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


class BST:
    def __init__(self):
        self.root = None
        self.nodes = {}

    def add(self, x):
        node = Node(x)
        self.nodes[x] = node

        if self.root is None:
            self.root = node
            return

        cur = self.root

        while True:
            if x < cur.key:
                if cur.left is None:
                    cur.left = node
                    node.parent = cur
                    return
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = node
                    node.parent = cur
                    return
                cur = cur.right

    def rotate_left(self, x):
        a = self.nodes[x]
        b = a.right
        parent = a.parent

        a.right = b.left
        if b.left is not None:
            b.left.parent = a

        b.left = a
        a.parent = b

        b.parent = parent

        if parent is None:
            self.root = b
        elif parent.left is a:
            parent.left = b
        else:
            parent.right = b

    def rotate_right(self, x):
        a = self.nodes[x]
        b = a.left
        parent = a.parent

        a.left = b.right
        if b.right is not None:
            b.right.parent = a

        b.right = a
        a.parent = b

        b.parent = parent

        if parent is None:
            self.root = b
        elif parent.left is a:
            parent.left = b
        else:
            parent.right = b

    def preorder(self):
        result = []
        stack = [self.root]

        while stack:
            node = stack.pop()
            result.append(str(node.key))

            if node.right is not None:
                stack.append(node.right)

            if node.left is not None:
                stack.append(node.left)

        return " ".join(result)


n = int(input())
keys = list(map(int, input().split()))

tree = BST()

for x in keys:
    tree.add(x)

m = int(input())

for _ in range(m):
    command, x = input().split()
    x = int(x)

    if command == "left":
        tree.rotate_left(x)
    else:
        tree.rotate_right(x)

    print(tree.preorder())