class ListNode:
    def __init__(self,value=0,next=None):
        self.value = value
        self.next = next
class Solution:
    def middleNode(self,head:ListNode)->ListNode:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
if __name__ == "__main__":
    head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
    sol = Solution()
    middle_node = sol.middleNode(head)
    print(middle_node.value)