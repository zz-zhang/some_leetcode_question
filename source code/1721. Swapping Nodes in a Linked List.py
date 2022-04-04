from random import randint
from utils import ListNode, build_list, print_list
from typing import Optional

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cache = []
        node = head
        while node is not None:
            cache.append(node)
            node = node.next
        if len(cache) == 1:
            return head
        if k == 1 or k == len(cache):
            if len(cache) > 1:
                cache[-2].next = cache[0]
            cache[0].next, cache[-1].next = cache[-1].next, cache[0].next
            head = cache[-1]
        else:
            cache[k - 2].next, cache[-k - 1].next = cache[-k - 1].next, cache[k - 2].next
            cache[-k].next, cache[k - 1].next = cache[k - 1].next, cache[-k].next
        return head

if __name__ == '__main__':
    sol = Solution()
    n = 1000
    lst = [randint(0, 100) for _ in range(n)]
    k = randint(1, n)
    head = build_list(lst)
    print_list(head)
    print(k)
    head = sol.swapNodes(head, k)
    # print_list(head)