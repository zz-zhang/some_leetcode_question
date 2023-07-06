class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if len(stack) == 0 or stack[-1] != char:
                stack.append(char)
            else:
                stack = stack[:-1]
        return ''.join(stack)

if __name__ == '__main__':
    sol = Solution()
    s = "a"
    print(sol.removeDuplicates(s))