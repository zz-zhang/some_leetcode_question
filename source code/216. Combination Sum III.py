from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # print(list(range(1, 10))[-k:], list(range(1, 10))[:k])
        if sum(list(range(1, 10))[-k:]) < n:
            return []
        if sum(list(range(1, 10))[:k]) > n:
            return []
        self.res = []
        self._search(list(range(1, 10)), n, k)
        return self.res

    def _search(self, nums, _sum, k, sub_res=[]):
        # breakpoint()
        for n in nums:
            if k == 1:
                if n == _sum:
                    self.res.append(sub_res + [n])
                    return
            else:
                if 9 - n >= k - 1:
                    self._search(list(range(n+1, 10)), _sum-n, k-1, sub_res + [n])

if __name__ == '__main__':
    sol = Solution()
    k = 5
    n = 20
    print(sol.combinationSum3(k, n))