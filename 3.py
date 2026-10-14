import sys

input = sys.stdin.readline


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def height(node):
    return node.height if node is not None else 0


def update_height(node):
    node.height = 1 + max(height(node.left), height(node.right))


def balance(node):
    return height(node.right) - height(node.left)


def rotate_left(a):
    b = a.right
    a.right = b.left
    b.left = a

    update_height(a)
    update_height(b)

    return b


def rotate_right(a):
    b = a.left
    a.left = b.right
    b.right = a

    update_height(a)
    update_height(b)

    return b


def rebalance(node):
    update_height(node)

    if balance(node) == 2:
        if balance(node.right) < 0:
            node.right = rotate_right(node.right)
        return rotate_left(node)

    if balance(node) == -2:
        if balance(node.left) > 0:
            node.left = rotate_left(node.left)
        return rotate_right(node)

    return node


def insert(node, key):
    if node is None:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    else:
        return node

    return rebalance(node)


def exists(node, key):
    while node is not None:
        if key == node.key:
            return True

        if key < node.key:
            node = node.left
        else:
            node = node.right

    return False


def preorder(root):
    if root is None:
        return "Empty"

    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(str(node.key))

        if node.right is not None:
            stack.append(node.right)

        if node.left is not None:
            stack.append(node.left)

    return " ".join(result)


q = int(input())
root = None
answers = []

for _ in range(q):
    command = input().split()

    if command[0] == "add":
        root = insert(root, int(command[1]))

    elif command[0] == "exists":
        x = int(command[1])
        answers.append("YES" if exists(root, x) else "NO")

    elif command[0] == "root":
        answers.append(str(root.key) if root is not None else "Empty")

    elif command[0] == "height":
        answers.append(str(height(root)))

    elif command[0] == "print":
        answers.append(preorder(root))

sys.stdout.write("\n".join(answers))