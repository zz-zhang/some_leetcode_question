class Solution:
    def checkRecord(self, s: str) -> bool:
        counter_a = 0
        counter_l = 0
        for char in s:
            if char == 'A':
                counter_a += 1
            if char == 'L':
                counter_l += 1
            else:
                 counter_l = 0

            if counter_a > 1 or counter_l > 2:
                return False
        if counter_a > 1 or counter_l > 2:
            return False
        return True

if __name__ == '__main__':
    sol = Solution()
    s = "AAPAPPPP"
    print(sol.checkRecord(s))