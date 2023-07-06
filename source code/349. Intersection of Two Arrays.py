from typing import List
from random import randint

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cache = set()
        for num in nums1:
            cache.add(num)

        res = set()
        for num in nums2:
            if num in cache:
                res.add(num)
        return list(res)


if __name__ == '__main__':
    sol = Solution()
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    nums1 = [randint(0, 1000) for _ in range(1000)]
    nums2 = [randint(0, 1000) for _ in range(1000)]
    print(nums1)
    print(nums2)
    print(sol.intersection(nums1, nums2))