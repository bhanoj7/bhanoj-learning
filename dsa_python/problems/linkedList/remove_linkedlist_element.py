# File: solution.py
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        nodes = []
        curr = self
        while curr:
            nodes.append(str(curr.val))
            curr = curr.next
        return " → ".join(nodes) + " → None"


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # FASTER: Two-pointer approach (0ms)
        while head and head.val == val:
            head = head.next

        cur = head
        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head


def create_list(values):
    """Helper: [1,2,3] → 1→2→3"""
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


# TEST CASES
def test_solution():
    sol = Solution()

    print("=== TEST 1: Remove 6 from [1,2,6,3,4,5,6] ===")
    head = create_list([1, 2, 6, 3, 4, 5, 6])
    print(f"Before: {head}")
    result = sol.removeElements(head, 6)
    print(f"After:  {result}")
    print()

    print("=== TEST 2: Remove head [1,2,6,3,4,6] ===")
    head = create_list([1, 2, 6, 3, 4, 6])
    print(f"Before: {head}")
    result = sol.removeElements(head, 1)
    print(f"After:  {result}")
    print()

    print("=== TEST 3: Remove all [1,1] ===")
    head = create_list([1, 1])
    print(f"Before: {head}")
    result = sol.removeElements(head, 1)
    print(f"After:  {result}")
    print()

    print("=== TEST 4: Empty list [] ===")
    head = None
    print(f"Before: {head}")
    result = sol.removeElements(head, 1)
    print(f"After:  {result}")


if __name__ == "__main__":
    test_solution()
