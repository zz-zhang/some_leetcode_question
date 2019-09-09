# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1_r = num1[::-1]
        num2_r = num2[::-1]
        res = [0 for _ in range(max(len(num1_r), len(num2_r)) + 1)]
        for i in range(len(res) - 1):
            if i < len(num1_r) and i < len(num2_r):
                res[i] += ord(num1_r[i]) + ord(num2_r[i]) - 2 * ord('0')
            elif i < len(num1_r):
                res[i] += ord(num1_r[i]) - ord('0')
            elif i < len(num2_r):
                res[i] += ord(num2_r[i]) - ord('0')
            if res[i] >= 10:
                res[i] -= 10
                res[i + 1] += 1
        res = [chr(item + ord('0')) for item in res]
        # print(res)
        if res[-1] == '0':
            res = ''.join(res[::-1])[1:]
        else:
            res = ''.join(res[::-1])
        return res


if __name__ == '__main__':
    sol = Solution()
    num1 = '5'
    num2 = '5'
    print(sol.addStrings(num1, num2))
