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
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            next_node = curr.next     # temporarily store next
            curr.next = prev          # reverse the pointer
            prev = curr               # move prev forward
            curr = next_node          # move curr forward

        return prev      # prev becomes the new head


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
    """Print the linked list."""
    curr = head
    out = []

    while curr:
        out.append(str(curr.val))
        curr = curr.next

    print(" -> ".join(out))


# ---------------------------
# Main (Run this in PyCharm)
# ---------------------------

if __name__ == "__main__":
    user_input = input("Enter linked list values (space-separated): ").strip()

    if not user_input:
        print("No input provided. Exiting.")
        exit()

    values = list(map(int, user_input.split()))

    print("\nInput Linked List:")
    print(values)

    head = build_linked_list(values)

    solver = Solution()
    reversed_head = solver.reverseList(head)

    print("\nReversed Linked List:")
    print_linked_list(reversed_head)
