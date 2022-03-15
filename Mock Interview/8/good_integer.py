'''
An integer x is a good if after rotating each digit individually by 180 degrees, we get a valid number that is different from x. Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. For example:

0, 1, and 8 rotate to themselves,
2 and 5 rotate to each other (in this case they are rotated in a different direction, in other words, 2 or 5 gets mirrored),
6 and 9 rotate to each other, and
the rest of the numbers do not rotate to any other number and become invalid.
Given an integer n, return the number of good integers in the range [1, n].'''

class Solution:
    def rotatedDigits(self, n):
        res = 0
        good_digits = '2569'
        not_bad_digits = '018'
        bad_digits = '347'
        for num in range(1, n + 1):
            num_str = self.num_to_str(num)
            good_flag = False
            for char in num_str:
                if char in bad_digits:
                    break
                if char in good_digits:
                    good_flag = True
            else:
                if good_flag:
                    res += 1
        return res
    
    def num_to_str(self, num):
        res = ''
        while num > 0:
            res = str(num % 10) + res
            num = int(num / 10)
        return res

if __name__ == '__main__':
    sol = Solution()
    n = 1
    print(sol.rotatedDigits(n))