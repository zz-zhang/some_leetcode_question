from utils import ListNode, build_list, print_list
from typing import Optional

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        stack_a, stack_b = [], []
        nodeA = headA
        while nodeA is not None:
            stack_a.append(nodeA)
            nodeA = nodeA.next

        nodeB = headB
        while nodeB is not None:
            stack_B.append(nodeB)
            nodeB = nodeB.next

        while len(stack_a) > 0 and len(stack_b) > 0:
            nodeA = stack_a[-1]
            nodeB = stack_b[-1]
            stack_a = stack_a[:-1]
            stack_b = stack_b[:-1]

        while nodeA is not None:
            if nodeA == nodeB:
                return nodeA
            nodeA = nodeA.next
            nodeB = nodeB.next

        return None
