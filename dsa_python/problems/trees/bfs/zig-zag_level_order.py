"""
WHAT: Return zigzag level order (alternate direction each level).
WHY: Demonstrates BFS level control and simple state toggling.
WHEN: Use for tree traversal problems, interview practice.
HOW: Use queue for BFS, collect each level into a list, reverse that list
     for every alternate level (when left_to_right == False).
Complexity: Time O(n), Space O(n) (queue + result).
"""

from collections import deque
from typing import Optional, List

# -------------------------
# Basic Tree node (local)
# -------------------------
class TreeNode:
    def __init__(self, val: int = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        q = deque([root])        # BFS queue
        result: List[List[int]] = []
        left_to_right = True     # start with left->right for level 0

        # Process level by level
        while q:
            level_size = len(q)    # number of nodes in current level
            level: List[int] = []  # collect node values for this level

            for _ in range(level_size):
                node = q.popleft()
                # record value
                level.append(node.val)

                # ALWAYS append children left then right to preserve BFS order
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # reverse the collected values if current level requires right->left
            if not left_to_right:
                level.reverse()

            result.append(level)
            left_to_right = not left_to_right  # toggle for next level

        return result


# -------------------------
# Quick local test
# -------------------------
if __name__ == "__main__":
    # Build test tree:
    #       3
    #      / \
    #     9  20
    #       /  \
    #      15   7
    root = TreeNode(3,TreeNode(9),TreeNode(20, TreeNode(15), TreeNode(7)))

    out = Solution().zigzagLevelOrder(root)
    print(out)  # Expected: [[3], [20, 9], [15, 7]]