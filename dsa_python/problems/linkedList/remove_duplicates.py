# ---------------------------
# Linked List Node Definition
# ---------------------------
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ---------------------------
# Solution Class
# ---------------------------
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head


# ---------------------------
# Helper Functions
# ---------------------------

# Convert Python list → Linked List
def build_linked_list(values):
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for v in values[1:]:
        current.next = ListNode(v)
        current = current.next

    return head


# Print Linked List
def print_linked_list(head):
    current = head
    out = []

    while current:
        out.append(current.val)
        current = current.next
    print(out)

# ---------------------------
# Main (Run this in PyCharm)
# ---------------------------
if __name__ == "__main__":
    user_input = input("Enter sorted numbers (space-separated): ").strip()

    if not user_input:
        print("Empty input! Exiting.")
        exit()

    # Convert "1 1 2 3 3" → [1, 1, 2, 3, 3]
    arr = list(map(int, user_input.split()))

    print("\nInput list:")
    print(arr)

    # Build linked list
    head = build_linked_list(arr)

    # Solve
    solver = Solution()
    result = solver.deleteDuplicates(head)

    print("\nOutput list:")
    print_linked_list(result)
