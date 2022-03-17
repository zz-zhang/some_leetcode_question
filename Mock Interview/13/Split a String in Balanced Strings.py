class Solution:
    def balancedStringSplit(self, s: str) -> int:
        stack = 0
        res = 0
        for idx, char in enumerate(s):
            if char == 'L':
                stack += 1
            if char == 'R':
                stack -= 1
            if stack == 0:
                # print(s, idx)
                res += 1
        return res

if __name__ == '__main__':
    sol = Solution()
    s = "RLRLRLRLLLRR"
    print(sol.balancedStringSplit(s))