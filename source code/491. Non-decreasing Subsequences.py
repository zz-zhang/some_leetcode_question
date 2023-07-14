from typing import List
from random import randint

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.hash_set = set()
        self.search(nums)
        return self.res
        
    def search(self, nums, sub_res=[]):
        if not nums:
            return
        for idx, n in enumerate(nums):
            if not sub_res or n >= sub_res[-1]:
                hash_code = sum([(num + 101) * 202 ** idx for idx, num in enumerate(sub_res + [n])])
                if sub_res and hash_code not in self.hash_set:
                    self.res.append(sub_res + [n])
                    self.hash_set.add(hash_code)
                    # print(hash_code)

                self.search(nums[idx+1:], sub_res + [n])
            

if __name__ == '__main__':
    sol = Solution()
    nums = [-1, 0, 0, 0]
    nums = [randint(-100, 100) for _ in range(15)]
    print(nums)
    print(sol.findSubsequences(nums))
