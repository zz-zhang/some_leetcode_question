
class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.replace('//', '/')
        paths = path.split('/')
        print(paths)
        res = []
        stack = []
        for p in paths:
            if len(p) > 0:
                if p == '.':
                    continue
                if p == '..':
                    if stack:
                        stack.pop(-1)
                else:
                    stack.append(p)
        while stack:
            res.append(stack.pop(-1))
        res.reverse()
        return '/' + '/'.join(res)

if __name__ == '__main__':
    sol = Solution()
    path = "/home//foo/..."
    print(sol.simplifyPath(path))