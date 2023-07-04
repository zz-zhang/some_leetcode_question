'''
solution in one pass
'''

from utils import ListNode, build_list, print_list
from typing import Optional

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cache = []
        node = head
        while node is not None:
            cache.append(node)
            node = node.next

        # for node in cache:
        #     print(node.val)
        cache = [None] + cache + [None]

        n = len(cache) - n - 1
        print(n)
        if n == 1:
            return cache[2]
        
        cache[n-1].next = cache[n+1]

        # breakpoint()
        return head


if __name__ == '__main__':
    sol = Solution()
    head = build_list([1,2])
    n = 1
    head = sol.removeNthFromEnd(head, n)

    print_list(head)