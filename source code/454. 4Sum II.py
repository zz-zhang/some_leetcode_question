from typing import List
from random import randint

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum_12 = {}
        sum_34 = {}

        for n1 in nums1:
            for n2 in nums2:
                if n1 + n2 in sum_12:
                    sum_12[n1 + n2] += 1
                else:
                    sum_12[n1 + n2] = 1

        for n1 in nums3:
            for n2 in nums4:
                if n1 + n2 in sum_34:
                    sum_34[n1 + n2] += 1
                else:
                    sum_34[n1 + n2] = 1

        res = 0
        for sum1, count1 in sum_12.items():
            for sum2, count2 in sum_34.items():
                if sum1 + sum2 == 0:
                    res += count1 * count2

        return res

if __name__ == '__main__':
    sol = Solution()
    nums1 = [0]
    nums2 = [2]
    nums3 = [0]
    nums4 = [0]

    n = 200
    limit = 100
    nums1 = [randint(int(-(limit)), int(limit)) for _ in range(n)]
    nums2 = [randint(int(-(limit)), int(limit)) for _ in range(n)]
    nums3 = [randint(int(-(limit)), int(limit)) for _ in range(n)]
    nums4 = [randint(int(-(limit)), int(limit)) for _ in range(n)]
    print(nums1, nums2, nums3, nums4, sep='\n')
    print(sol.fourSumCount(nums1, nums2, nums3, nums4))