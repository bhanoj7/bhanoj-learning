from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
def right_most_path(root):
    if not root:
        return []
    node = root
    result = []
    while node:
        result.append(node.val)
        if node.right:
            node = node.right
        else:
            node = node.left
    return result

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    print(right_most_path(root))