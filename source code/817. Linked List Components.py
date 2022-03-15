# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def create_by_list(l):
        head = ListNode(l[0])
        node = head
        for num in l[1:]:
            node.next = ListNode(num)
            node = node.next
        return head

class Solution:
    def numComponents(self, head, nums):
        recoder = ''
        node = head
        while node is not None:
            if node.val in nums:
                recoder = recoder + '1'
            else:
                recoder = recoder + '0'
            node = node.next
        # print(recoder)
        while '00' in recoder:
            recoder = recoder.replace('00', '0')
        if recoder[0] == '0':
            recoder = recoder[1:]
        if recoder[-1] == '0':
            recoder = recoder[:-1]
        # print(recoder.split('0'))
        return len(recoder.split('0'))

if __name__ == '__main__':
    sol = Solution()
    head = ListNode.create_by_list([0,1,2,3,4])
    nums=[0,1,3]
    print(sol.numComponents(head, nums))
