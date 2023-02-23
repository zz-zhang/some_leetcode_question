from utils import TreeNodeFor116


class Solution:
    def connect(self, root):
        if root is None:
            return None
        depth_order_list = self.get_depth_order(root)
        for (node1, d1), (node2, d2) in zip(depth_order_list[:-1],
                                            depth_order_list[1:]):
            if d1 == d2:
                node1.next = node2
                # print(node1.val, node2.val)
        return root

    def get_depth_order(self, root):
        q = [(root, 0)]
        res = []
        while len(q) > 0:
            node, depth = q[0]
            if node.left is not None:
                q.append((node.left, depth + 1))
            if node.right is not None:
                q.append((node.right, depth + 1))
            res.append((node, depth))
            q = q[1:]
        return res


if __name__ == '__main__':
    sol = Solution()
    inp = '[1,2,3,4,5,6,7]'
    root = TreeNodeFor116.build_by_str(inp)
    res = sol.connect(root)
    if res is not None:
        print(res.get_next_list())
