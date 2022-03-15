from xml.dom.minicompat import EmptyNodeList


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_list(self):
        print(self.val, end=' ')
        node = self.next
        while node is not None:
            print(node.val, end=' ')
            node = node.next
        print()

    def create_by_list(l):
        head = ListNode(l[0])
        node = head
        for num in l[1:]:
            node.next = ListNode(num)
            node = node.next
        return head

class Solution:
    def removeZeroSumSublists(self, head):
        empty_node = ListNode(-13, head)
        start_node = empty_node

        while start_node is not None:
            node = start_node.next
            s = 0
            del_flag = False
            while node is not None:
                s += node.val
                if s == 0:
                    start_node.next = node.next
                    start_node = empty_node
                    del_flag = True
                    break
                node = node.next
        
            # empty_node.print_list()

            if not del_flag:
                start_node = start_node.next
        return empty_node.next

if __name__ == '__main__':
    sol = Solution()
    lst = [0, 0]
    head = ListNode.create_by_list(lst)
    res = sol.removeZeroSumSublists(head)
    if res != None:
        res.print_list()
    else:
        print([])