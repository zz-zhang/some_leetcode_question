from typing import List
from random import randint

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        lengths = []
        start = 0
        while start < len(nums):
            if nums[start] == 0:
                end = start + 1
                while end < len(nums) and nums[end] == 0:
                    end += 1
                lengths.append(end - start)
                start = end
            else:
                start += 1
        # print(lengths)
        res = 0
        for l in lengths:
            res += self.add2one(l)
        return res

    def add2one(self, num):
        if num == 1:
            return num
        else:
            return num + self.add2one(num - 1)
        

if __name__ == '__main__':
    sol = Solution()
    nums = [2,10,2019]
    nums = [randint(-10, 10) for _ in range(100)]
    print(nums)
    print(sol.zeroFilledSubarray(nums))