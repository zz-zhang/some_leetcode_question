from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = set()
        self._combine(list(range(1, n+1)), k)
        self.res = sorted(self.res)
        return self.res

    def _combine(self, nums, k, sub_res=[]):
        # breakpoint()
        if k == 0:
            self.res.add(tuple(sub_res))
        for idx, n in enumerate(nums):
            if len(nums[idx+1:]) >= k - 1: 
                self._combine(nums[idx+1:], k-1, sub_res + [n])

if __name__ == '__main__':
    sol = Solution()
    n = 4
    k = 2
    print(sol.combine(n, k))