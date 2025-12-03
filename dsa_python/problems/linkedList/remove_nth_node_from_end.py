class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 1. dummy node before head
        dummy = ListNode(0, head)

        slow = dummy
        fast = dummy

        # 2. move fast n+1 steps
        for _ in range(n + 1):
            fast = fast.next

        # 3. move both pointers
        while fast:
            slow = slow.next
            fast = fast.next

        # 4. delete node
        slow.next = slow.next.next

        # 5. return new head
        return dummy.next


# ----------- Testing in PyCharm ------------
def print_list(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


if __name__ == "__main__":
    # create linked list: 1→2→3→4→5
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    sol = Solution()
    new_head = sol.removeNthFromEnd(n1, 2)
    print_list(new_head)
