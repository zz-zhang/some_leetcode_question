'''
Given the root of a Binary Search Tree and a target number k, 
return true if there exist two elements in the BST such that 
their sum is equal to the given target.
'''
# Definition for a binary tree node.
from xxlimited import Null


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def list_to_tree(self, numbers):
        root = TreeNode()
        currect = root
        treelist = []
        for idx, val in enumerate(numbers):
            if val is not None:
                treelist.append(TreeNode(val))
            else:
                treelist.append(None)

        # breakpoint()
        for idx, curr in enumerate(treelist):
            if curr is not None:
                if idx * 2 + 1 < len(treelist) and treelist[idx * 2 + 1] is not None:
                    curr.left = treelist[idx * 2 + 1]
                if idx * 2 + 2 < len(treelist) and treelist[idx * 2 + 2] is not None:
                    curr.right = treelist[idx * 2 + 2]
        # breakpoint()
        return treelist[0]

    def travel(self):
        print(self.val, end=' ')
        if self.left is not None:
            self.left.travel()
        else:
            print('None', end=' ')
        if self.right is not None:
            self.right.travel()
        else:
            print('None', end=' ')

class Solution:
    def findTarget(self, root, k):
        numbers = self.bfs(root)
        for num in numbers:
            tgt = k - num
            # print(num, tgt)
            # breakpoint()
            if tgt == num:
                 continue
            if self.search(root, tgt):
                return True
        return False
        
    def bfs(self, node):
        q = [node]
        head = 0
        tail = 0
        res = []
        while len(q) > 0:
            if q[0].left is not None:
                q.append(q[0].left)
            if q[0].right is not None:
                q.append(q[0].right)
            # print(q[0].val, end=' ')
            res.append(q[0].val)
            q = q[1:]
        return res

    def search(self, node, tgt):
        # print(node.val, tgt)
        if tgt == node.val:
            return True
        elif tgt < node.val:
            if node.left is not None:
                return self.search(node.left, tgt)
            else:
                return False
        else:
            if node.right is not None:
                return self.search(node.right, tgt)
            else:
                return False

    
if __name__ == '__main__':
    sol = Solution()
    root = [2, 1, 3]
    k = 4
    node = TreeNode().list_to_tree(root)

    print(sol.findTarget(node, k))
