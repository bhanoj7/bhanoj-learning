# ---------------- List Node Definition ---------------- #

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ---------------- Solution Class ---------------- #

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy
        carry = 0

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + carry
            digit = total % 10
            carry = total // 10

            tail.next = ListNode(digit)
            tail = tail.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


# ---------------- Helper Functions ---------------- #

def build_list(values):
    """Builds a linked list from a Python list"""
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def print_list(node):
    """Prints a linked list"""
    while node:
        print(node.val, end=" ")
        node = node.next
    print()


# ---------------- Example / Test ---------------- #

if __name__ == "__main__":
    # Example: l1 = [2,4,3], l2 = [5,6,4]
    l1 = build_list([2, 4, 3])
    l2 = build_list([5, 6, 4])

    sol = Solution()
    result = sol.addTwoNumbers(l1, l2)

    print("Result:")
    print_list(result)
    # Expected output: 7 0 8
