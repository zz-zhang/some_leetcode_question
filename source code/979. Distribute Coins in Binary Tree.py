# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def distributeCoins(self, root):
        q = [root]
        req, hav = self.require_and_have(root, root.val)
        require = [req]
        have = [hav]
        res = 0
        while len(q) > 0:
            # print(require, have)
            if q[0].left is not None:
                req, hav = self.require_and_have(q[0].left, q[0].left.val)
                require.append(req)
                have.append(hav)
                q.append(q[0].left)
                res += abs(req - hav)
                q[0].left.val = req
                # print('left', req, hav, q[0].left.val)
                
            if q[0].right is not None:
                req, hav = self.require_and_have(q[0].right, q[0].right.val)
                require.append(req)
                have.append(hav)
                q.append(q[0].right)
                res += abs(req - hav)
                q[0].right.val = req  
                # print('right', req, hav, q[0].right.val)

            q = q[1:]
            require = require[1:]
            have = have[1:]
        return res

    
    def require_and_have(self, node, have, require=1):
        total_req = require
        if node.left is not None:
            req, hav = self.require_and_have(node.left, node.left.val, require)
            total_req += req
            have = have + hav
        if node.right is not None:
            req, hav = self.require_and_have(node.right, node.right.val, require)
            total_req += req
            have = have + hav
        
        # print(node.val, have, total_req)
        return total_req, have

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(2)

    print(sol.distributeCoins(root))