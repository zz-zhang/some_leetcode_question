class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        if len(s) > 0 and s[0] == '-':
            s = '~' + s[1:]
        print(s)
        polish_notation = self.to_polish_notation(s)
        print(polish_notation)

        stack = []
        for item in polish_notation:
            if isinstance(item, int):
                stack.append(item)
            elif item == '+':
                res = stack.pop(-1) + stack.pop(-1)
                stack.append(res)
            elif item == '-':
                res = stack.pop(-1) - stack.pop(-1)
                stack.append(res)
            elif item == '~':
                stack[-1] = -stack[-1]
        return stack.pop(-1)

    def to_polish_notation(self, s):
        idx = len(s) - 1
        stack = []
        res = []
        while idx >= 0:
            if s[idx] not in '+-()~':
                start = idx
                while start >= 0 and s[start] not in '+-()~':
                    start -= 1
                
                if start >= 0 and s[start] == '-':
                    if start - 1 < 0:
                        start -= 1
                    elif s[start - 1] in '(':
                        start -= 1

                res.append(int(s[start+1: idx+1]))
                idx = start
                continue
            if s[idx] in '+~':
                stack.append(s[idx])
            elif s[idx] == '-':
                # breakpoint()
                if idx > 0 and s[idx - 1] == '(':
                    stack.append('~')
                else:
                    stack.append('-')
            elif s[idx] == ')':
                stack.append(s[idx])
            else:
                while stack and stack[-1] != ')':
                    res.append(stack.pop(-1))
                stack.pop(-1)
            idx -= 1
        while stack:
            res.append(stack.pop(-1))
        return res



if __name__ == '__main__':
    sol = Solution()
    s = "- (3 - (- (4 + 5) ) )"
    print(sol.calculate(s))