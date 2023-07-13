from typing import List
from random import randint

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        self.res = []
        self.search(candidates, target)
        return self.res

    def search(self, candidates, target, sub_res=[]):
        for idx, num in enumerate(candidates):
            if idx > 0 and candidates[idx - 1] == num:
                continue
            if num == target:
                self.res.append(sub_res + [num])
                return
            if num > target:
                return
            if sum(candidates[idx+1:]) >= target - num:
                self.search(candidates[idx+1:], target - num, sub_res + [num])

    def list_equal(self, lst1, lst2):
        if len(lst1) != len(lst2):
            return False
        for n1, n2 in zip(lst1, lst2):
            if n1 != n2:
                return False
        return True

if __name__ == '__main__':
    sol = Solution()
    candidates = [1, 1, 1]
    target = 4
    # candidates = [randint(1, 50) for _ in range(100)]
    # target = 30
    print(candidates)
    print(target)
    print(sol.combinationSum2(candidates, target))
