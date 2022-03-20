from random import randint
from typing import *
from utils import *
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        num = 0
        node = head
        while node is not None:
            node = node.next
            num += 1
        # print(num)

        q = []
        s = []
        node = head
        counter = 0
        while node is not None:
            if counter < (num / 2):
                q.append(node)
            else:
                s.append(node)
            counter += 1
            node = node.next

        # for node in q:
        #     print(node.val, end = ' ')
        # print()
        # for node in s:
        #     print(node.val, end = ' ')
        # print()

        while len(s) > 0:
            if len(s) > 0:
                q[0].next = s[-1]
            else:
                q[0].next = None
            q = q[1:]
            
            if len(q) > 0:
                s[-1].next = q[0]
            else:
                s[-1].next = None
            s = s[:-1]
        if len(q) > 0:
            q[0].next = None
        return head


if __name__ == '__main__':
    sol = Solution()
    # lst = [randint(1, 1000) for _ in range(1000)]
    lst = [1,2,3,4,5]
    print(lst)
    head = build_list(lst)
    sol.reorderList(head)
    print_list(head)