from distutils import dir_util
from random import randint


class Solution:
    def smallestNumber(self, num: int):
        flag = 1 if num >= 0 else -1
        num = abs(num)
        digits = list(str(num))
        # print(digits)

        if flag == 1:
            digits = sorted(digits)
            i = 0
            while i < len(digits) and digits[i] == '0':
                i += 1
            # print(i, digits[i])
            if i < len(digits):
                digits[0], digits[i] = digits[i], digits[0]
        else:
            digits = sorted(digits, reverse=True)
        # print(digits)
        res = sum([int(dig) * 10 ** (len(digits) - 1 - idx) for idx, dig in enumerate(digits)])

        return flag * res

if __name__ == '__main__':
    sol = Solution()
    for _ in range(5):
        num = randint(-10 ** 15, 10 ** 15)
        print(sol.smallestNumber(num))
        