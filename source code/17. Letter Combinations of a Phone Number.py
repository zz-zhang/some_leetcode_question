from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.dig2chars = {
            dig: ''.join([chr(97 + 3 * (dig - 1) - 3 + i) for i in range(3)]) for dig in range(2, 7)
        }
        self.dig2chars[7] = 'pqrs'
        self.dig2chars[8] = 'tuv'
        self.dig2chars[9] = 'wxyz'

        self.res = []
        self.search(digits)
        return self.res
        
    def search(self, digits, sub_res=''):
        if len(digits) == 0:
            if sub_res:
                self.res.append(sub_res)
            return

        num = int(digits[0])
        for char in self.dig2chars[num]:
            self.search(digits[1:], sub_res + char)


if __name__ == '__main__':
    sol = Solution()
    digits = "9876"
    print(sol.letterCombinations(digits))