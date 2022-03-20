from typing import *
from utils import build_list, ListNode, print_list
from random import randint

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev_node = ListNode(-1)
        prev_node.next = head
        new_head = prev_node
        while node is not None:
            # breakpoint()
            if node.next is not None and node.val == node.next.val:
                while node.next is not None and node.val == node.next.val:
                    node = node.next
                prev_node.next = node.next
                node = node.next
            else:
                prev_node = node
                node = node.next
            # print(prev_node.val)
        print_list(new_head.next)
        return new_head.next



if __name__ == '__main__':
    sol = Solution()
    lst = sorted([randint(-100, 100) for _ in range(300)])
    # lst = [1,2,3]
    print(lst)
    head = build_list([])
    sol.deleteDuplicates(head)