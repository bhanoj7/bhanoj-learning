# ---------------------------
# ListNode Definition
# ---------------------------
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ---------------------------
# Solution Class
# ---------------------------
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Dummy node to build the merged list
        dummy = ListNode()
        tail = dummy
        # Merge while both lists have elements
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Attach remaining nodes from either list
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next


# ---------------------------
# Helper Functions
# ---------------------------
def build_linked_list(values):
    """Convert Python list to linked list."""
    if not values:
        return None

    head = ListNode(values[0])
    curr = head

    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next

    return head


def print_linked_list(head):
    """Print linked list as 'a -> b -> c'."""
    if not head:
        print("Empty List")
        return

    curr = head
    res = []
    while curr:
        res.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(res))


# ---------------------------
# Main (Run in PyCharm)
# ---------------------------
if __name__ == "__main__":
    # Input example: 1 2 4
    list1_input = input("Enter sorted list1 values (space-separated): ").strip()
    list2_input = input("Enter sorted list2 values (space-separated): ").strip()

    list1_vals = list(map(int, list1_input.split())) if list1_input else []
    list2_vals = list(map(int, list2_input.split())) if list2_input else []

    list1 = build_linked_list(sorted(list1_vals))
    list2 = build_linked_list(sorted(list2_vals))

    print("\nList 1:")
    print_linked_list(list1)

    print("\nList 2:")
    print_linked_list(list2)

    solver = Solution()
    merged = solver.mergeTwoLists(list1, list2)

    print("\nMerged List:")
    print_linked_list(merged)
