from typing import List
from random import randint

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cache = {char: 0 for char in nums1}
        for num in nums1:
            cache[num] += 1

        res = []
        for num in nums2:
            if num in cache and cache[num] > 0:
                res.append(num)
                cache[num] -= 1
        return list(res)


if __name__ == '__main__':
    sol = Solution()
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    nums1 = [randint(0, 1000) for _ in range(1000)]
    nums2 = [randint(0, 1000) for _ in range(1000)]
    print(nums1)
    print(nums2)
    print(sol.intersect(nums1, nums2))