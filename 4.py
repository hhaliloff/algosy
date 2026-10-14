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


def find_min(node):
    while node.left is not None:
        node = node.left
    return node


def remove_min(node):
    if node.left is None:
        return node.right

    node.left = remove_min(node.left)
    return rebalance(node)


def delete(node, key):
    if node is None:
        return None

    if key < node.key:
        node.left = delete(node.left, key)

    elif key > node.key:
        node.right = delete(node.right, key)

    else:
        if node.left is None:
            return node.right

        if node.right is None:
            return node.left

        minimum = find_min(node.right)

        node.key = minimum.key
        node.right = remove_min(node.right)

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


def next_key(node, key):
    result = None

    while node is not None:
        if node.key >= key:
            result = node.key
            node = node.left
        else:
            node = node.right

    return result


def prev_key(node, key):
    result = None

    while node is not None:
        if node.key <= key:
            result = node.key
            node = node.right
        else:
            node = node.left

    return result


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
    operation = command[0]

    if operation == "add":
        root = insert(root, int(command[1]))

    elif operation == "del":
        root = delete(root, int(command[1]))

    elif operation == "exists":
        x = int(command[1])
        answers.append("YES" if exists(root, x) else "NO")

    elif operation == "next":
        x = int(command[1])
        result = next_key(root, x)
        answers.append(str(result) if result is not None else "None")

    elif operation == "prev":
        x = int(command[1])
        result = prev_key(root, x)
        answers.append(str(result) if result is not None else "None")

    elif operation == "root":
        answers.append(str(root.key) if root is not None else "Empty")

    elif operation == "height":
        answers.append(str(height(root)))

    elif operation == "print":
        answers.append(preorder(root))

sys.stdout.write("\n".join(answers))