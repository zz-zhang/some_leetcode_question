'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.
'''

class Solution:
    def hammingDistance(self, x: int, y: int):
        x = self.num_to_binary_str(x)
        # print(x)
        y = self.num_to_binary_str(y)
        # print(y)
        res = 0
        for char1, char2 in zip(x, y):
            if char1 != char2:
                res += 1
        return res

    def num_to_binary_str(self, num):
        res = ''
        div = 31
        while num > 0:
            # print(num, 2 ** div)
            if num >= (2 ** div):
                res = res + '1'
                num -= (2 ** div)
            else:
                res = res + '0'
            div -= 1
        while len(res) < 32:
            res = res + '0'
        return res

if __name__ == '__main__':
    sol = Solution()
    x = 2 ** 31 - 1
    y = 0
    print(sol.hammingDistance(x, y))