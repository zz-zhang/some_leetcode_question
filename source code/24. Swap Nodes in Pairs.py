
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        num = 1
        p = head
        while p.next != None:
            p = p.next
            num += 1
        lst = []
        p = head
        while p != None:
            lst.append(p)
            p = p.next
        i = 0
        if head.next != None:
            head = head.next


        while i < len(lst):
            if i % 2 == 0:
                if i + 3 < len(lst):
                    lst[i].next = lst[i + 3]
                elif i + 2 < len(lst):
                    lst[i].next = lst[i + 2]
                else:
                    lst[i].next = None
            else:
                lst[i].next = lst[i - 1]
            i += 1
        return head

if __name__ == '__main__':
    sol = Solution()
    head = ListNode(1)
    p = head
    # for i in range(2, 6):
    #     p.next = ListNode(i)
    #     p = p.next
    head = sol.swapPairs(head)

    p = head
    while p != None:
        print(p.val)
        p = p.next