from utils import ListNode, build_list, print_list
from typing import Optional

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        faster, slower = head, head

        while faster is not None:
            if faster.next is None:
                return -1
            faster = faster.next.next
            slower = slower.next
            if faster == slower:
                break

        meet_node = faster
        node = head
        while meet_node != node:
            meet_node = meet_node.next
            node = node.next
        return node


if __name__ == '__main__':
    sol = Solution()
    head = build_list([1,2])
    n = 1
    head = sol.detectCycle(head, n)

    print_list(head)