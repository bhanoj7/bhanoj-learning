class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: [ListNode], k: int) -> [ListNode]:
        if not head or not head.next:
            return head

        # compute length
        length = 1
        p = head
        while p.next:
            p = p.next
            length += 1
        tail = p

        # reduce k
        k = k % length
        if k == 0:
            return head

        # make circular
        tail.next = head

        # find new tail
        new_tail_pos = length - k - 1
        new_tail = head
        for _ in range(new_tail_pos):
            new_tail = new_tail.next

        # new head
        new_head = new_tail.next

        # break
        new_tail.next = None

        return new_head

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
    rotateRight = solver.rotateRight(head,2)

    print("\nReversed Linked List:")
    print_linked_list(rotateRight)