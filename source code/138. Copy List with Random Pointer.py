class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node = head
        node_list = []
        while node is not None:
            node_list.append(node)
            node = node.next

        new_node_list = [Node(10001) for _ in range(len(node_list))] + [None]

        for idx in range(len(node_list)):
            new_node_list[idx].val = node_list[idx].val
            new_node_list[idx].next = new_node_list[idx + 1]
            if node_list[idx].random:
                new_node_list[idx].random = new_node_list[node_list.index(node_list[idx].random)]
            else:
                new_node_list[idx].random = None
        return new_node_list[0]

    def _get_idx(self, node, key):
        idx = 0
        while node is not None:
            if node.val == key:
                return idx
            idx += 1
            node = node.next
        else:
            return None