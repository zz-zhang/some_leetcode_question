from utils import ListNode, build_list, print_list
from typing import Optional
from random import randint
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        node = head
        prev = None
        while node is not None:
            if node.val == val:
                if prev is None:
                    head = head.next
                else:
                    prev.next = node.next
            else:
                prev = node
            node = node.next
        return head
            


if __name__ == '__main__':
    sol = Solution()
    head = build_list([1,2,6,3,4,5,6])
    val = 6

    head_lst = [randint(1, 50) for _ in range(1000)]
    head = build_list(head_lst)
    val = 50
    print(head_lst)

    head = sol.removeElements(head, val)
    print_list(head)