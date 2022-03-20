from random import randint
from typing import *
from utils import build_list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        res = []
        node = head
        idx = 0
        while node is not None:
            while len(stack) > 0 and node.val > stack[-1][0].val:
                last_idx = stack[-1][1]
                stack = stack[:-1]
                res[last_idx] = node.val
            stack.append((node, idx))
            node = node.next
            idx += 1
            res.append(0)
        # print(res)
        return res


if __name__ == '__main__':
    sol = Solution()
    lst = [randint(1, 100) for _ in range(10 ** 4)]
    print(lst)
    head = build_list(lst)
    print(sol.nextLargerNodes(head))