from utils import ListNode, build_list, print_list
from typing import Optional

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # return self.quick_sort(head, None)
        return self.mergeSort(head)

    def mergeSort(self, head: Optional[ListNode]):
        if not head or not head.next:
            return head
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        left_head = head
        right_head = slow.next

        slow.next = None

        left = self.mergeSort(left_head)
        right = self.mergeSort(right_head)
        # self.printout(left, None)
        # self.printout(right, None)

        merged = self.merge(left, right)
        # self.printout(merged, None)
        return merged

    def merge(self, left: Optional[ListNode], right: Optional[ListNode]):
        dummy = ListNode(10001)
        cur = dummy
        while left and right:
            if left.val <= right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next

        while left:
            cur.next = left
            left = left.next
            cur = cur.next

        while right:
            cur.next = right
            right = right.next
            cur = cur.next

        return dummy.next

    def partition(self, left: Optional[ListNode], right: Optional[ListNode]):
        if left == right or left.next == right:
            return left
        pivot = left

        node_i, node_j = left, left.next
        while node_j != right:
            if node_j.val < pivot.val:
                node_i = node_i.next
                node_i.val, node_j.val = node_j.val, node_i.val
            node_j = node_j.next

        node_i.val, pivot.val = pivot.val, node_i.val
        return node_i

    def quick_sort(self, left: Optional[ListNode], right: Optional[ListNode]):
        if left == right or left.next == right:
            return left

        pivot = self.partition(left, right)
        self.quick_sort(left, pivot)
        self.quick_sort(pivot.next, right)
        return left

    def printout(self, left, right):
        node = left
        while node and node != right:
            print(node.val, end=', ')
            node = node.next
        print()


if __name__ == '__main__':
    sol = Solution()
    head = [-1,5,3,4,0]
    head = build_list(head)
    head = sol.sortList(head)

    print_list(head)