class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        s = list(s)
        i = 0
        while i < len(s):
            if s[i] == '(' and s[i + 1]  == ')':
                s = s[: i] + [1] + s[i + 2:]
            else:
                i += 1
        
        while '(' in s:
            i = 0
            while '(' in s and i < len(s):
                # breakpoint()
                if s[i] == '(' and isinstance(s[i + 1], int) and s[i + 2] == ')':
                    s = s[: i] + [2 * s[i + 1]] + s[i + 3:]
                elif isinstance(s[i], int) and i + 1 < len(s) and isinstance(s[i + 1], int):
                    s = s[: i] + [s[i] + s[i + 1]] + s[i + 2:]
                else:
                    i += 1
                print(s)
        print(s)
        return sum(s)

        

if __name__ == '__main__':
    sol = Solution()
    s = "(" * 25 + ')' * 25
    print(sol.scoreOfParentheses(s))