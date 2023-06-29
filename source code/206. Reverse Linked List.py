from utils import ListNode, build_list, print_list
from typing import Optional
import random

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev = None
        while node is not None:
            nxt = node.next

            node.next = prev
            prev = node
            node = nxt
        return prev

if __name__ == '__main__':
    sol = Solution()
    lst = [random.randint(-5000, 5000) for _ in range (100)]
    print(lst)
    head = build_list(lst)
    # head = build_list(head)
    res = sol.reverseList(head)
    # breakpoint()
    print_list(res)