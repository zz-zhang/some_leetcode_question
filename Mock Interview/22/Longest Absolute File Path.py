class Solution:
    def lengthLongestPath(self, input: str) -> int:
        inp = input.split('\n')
        # print(inp)
        stack = [('', -1)]
        res = 0
        for path in inp:
            if len(path) == 0:
                continue
            depth = path.count('\t')
            # print(path, depth)
            if len(stack) > 0:
                _, prev_depth = stack[-1]
                while len(stack) > 0 and prev_depth + 1 != depth:
                    stack.pop()
                    if len(stack) > 0:
                        _, prev_depth = stack[-1]
                if '.' in path:
                    full_path = '/'.join([p.replace('\t', '') for p, _ in stack] + [path.replace('\t', '')])
                    print(full_path)
                    length = sum([len(p.replace('\t', '')) + 1 for p, _ in stack]) + len(path.replace('\t', '')) - 1
                    res = max(res, length)
                else:
                    stack.append((path, depth))
            else:
                if '.' in path:
                    full_path = '/'.join([p.replace('\t', '') for p, _ in stack] + [path.replace('\t', '')])
                    print(full_path)
                    length = sum([len(p.replace('\t', '')) + 1 for p, _ in stack]) + len(path.replace('\t', '')) - 1
                    res = max(res, length)
                stack.append((path, depth))
        return res


if __name__ == '__main__':
    sol = Solution()
    inp = "a"

    print(sol.lengthLongestPath(inp))