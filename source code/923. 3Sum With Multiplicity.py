from random import randint, shuffle
from typing import List

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        from collections import defaultdict
        nums = defaultdict(int)
        for num in arr:
            nums[num] += 1
        res = 0
        visited = []
        keys = sorted(list(nums.keys()))
        for n1_ in keys:
            for n2_ in keys:
                # print(n1_, n2_)
                # breakpoint()
                if n1_ == n2_ and nums[n1_] == 1:
                    continue
                sub_tgt = target - n1_ - n2_
                idx = self.binary_search(keys, sub_tgt)
                if idx != -1:
                    n3_ = keys[idx]
                    n1, n2, n3 = sorted([n1_, n2_, n3_])
                    if (n1, n2, n3) in visited:
                        continue
                    visited.append((n1, n2, n3))
                    if n1 == n2 and nums[n1] < 2:
                        continue
                    if n2 == n3 and nums[n2] < 2:
                        continue
                    if n1 == n3 and nums[n1] < 3:   # n1 == n2 == n3
                        continue
                    
                    # print(n1, n2, n3)
                    if n1 != n2 and n2 == n3:
                        # breakpoint()
                        res += nums[n1] * self.comb(nums[n2], 2)
                    elif n1 == n2 and n2 != n3:
                        res += self.comb(nums[n1], 2) * nums[n3]
                    elif n1 == n3:
                        res += self.comb(nums[n1], 3)
                    else:
                        res += nums[n1] * nums[n2] * nums[n3]
                    res %= (10 ** 9 + 7)
                    # print(res)
        return res

    def binary_search(self, nums, tgt):
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == tgt:
                return mid
            if nums[mid] < tgt:
                i = mid + 1
            else:
                j = mid
            if i == j and nums[i] != tgt:
                return -1
        return -1

    def comb(self, n, m):
        if n == m:
            return 1
        elif m == 1:
            return n
        else:
            return (self.comb(n - 1, m - 1) + self.comb(n - 1, m)) % (10 ** 9 + 7)

if __name__ == '__main__':
    sol = Solution()
    arr = sorted([randint(0, 100) for _ in range(3000)])
    target = randint(0, 200)
    print(arr)
    print(target)
    print(sol.threeSumMulti(arr, target))
    # arr = [i for i in range(100)]
    # idx = sol.binary_search(arr, 99)
    # print(idx, arr[idx])