# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        val_list = []
        res_list = []
        node = head
        while node is not None:
            val_list.append(node.val)
            node = node.next
        start_index = 0
        while start_index + k <= len(val_list):
            res_list += val_list[start_index : start_index + k][::-1]
            start_index += k
        res_list += val_list[start_index:]
        # print(res_list)
        res = ListNode(-1)
        node = res
        for item in res_list:
            node.next = ListNode(item)
            node = node.next
        res = res.next
        return res


if __name__ == '__main__':
    s = Solution()
    input_list = [1, 2, 3, 4, 5]
    head = ListNode(-1)
    node = head
    for item in input_list:
        node.next = ListNode(item)
        node = node.next
    head = head.next
    print(s.reverseKGroup(head, 2))