from typing import List
from random import randint, choice

class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = []
        while n:
            digits.append(n % 10)
            n //= 10
        # print(digits)
        nine_flag = -1
        for idx in range(len(digits)):
            if idx + 1 < len(digits):
                if digits[idx] < digits[idx + 1]:
                    digits[idx] = 9
                    nine_flag = idx
                    digits[idx + 1] -= 1
        # print(digits)
        if nine_flag != -1:
            for idx in range(nine_flag):
                digits[idx] = 9
        res = 0
        for idx, d in enumerate(digits):
            res += d * 10 ** idx
        return res

if __name__ == '__main__':
    sol = Solution()
    n = 65525
    print(n)
    print(sol.monotoneIncreasingDigits(n))