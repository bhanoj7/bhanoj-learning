from collections import deque
import math

class TreeNode:
    def __init__(self,val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
def max_per_levl(root):
    if not root: return []
    q = deque([root])
    result = []
    while q:
        level_size = len(q)
        max_val = -math.inf
        for _ in range(level_size):
            node = q.popleft()
            max_val = max(max_val,node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(max_val)
    return result

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(max_per_levl(root))