from utils import TreeNode

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.counter = 0
        self.res = None
        self.lrd(root, [p, q])  # if p and q are ints
        # self.lrd(root, [p.val, q.val])  # if p and q are Treenodes
        return self.res

    def lrd(self, node, pq):
        children = {node.val}
        if node.left is not None:
            ch_of_ch = self.lrd(node.left, pq)
            children.add(node.left.val) 
            children = children.union(ch_of_ch)
        if node.right is not None:
            ch_of_ch = self.lrd(node.right, pq)
            children.add(node.right.val) 
            children = children.union(ch_of_ch)
        if node.val in pq:
            self.counter += 1
        # print(node.val, self.counter, children)
        if self.counter == 2:
            if self.res is None and p in children and q in children:
                self.res = node
        return children
        

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode.build_by_str('[3,5,1,6,2,0,8,null,null,7,4]')
    p = 5
    q = 1
    print(sol.lowestCommonAncestor(root, p, q).val)