# Definition for singly-linked list.
from random import randint
from typing import *
from utils import *

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        length = 1
        node = head
        while node.next is not None:
            # prev = node
            node = node.next
            length += 1
        k = k % length
        # print(length, k)
        if k == 0:
            return head

        node = head
        prev = None
        while (length - k) > 0:
            prev = node
            node = node.next
            k += 1
        prev.next = None
        res = node
        # print(node.val, prev.val)
        while node.next is not None:
            node = node.next
            # print(node.val)
        node.next = head
        return res

if __name__ == '__main__':
    sol = Solution()
    lst = [randint(-100, 100) for _ in range(500)]
    print(lst)
    head = build_list(lst)
    k = 2000000000
    head = sol.rotateRight(head, k)
    print_list(head)