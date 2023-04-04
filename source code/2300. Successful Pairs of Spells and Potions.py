from typing import List
from random import randint

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions = sorted(potions)
        potions = potions
        # print(potions)
        for sp in spells:
            start = 0
            end = len(potions) - 1
            while start <= end:
                mid = (start + end) // 2
                if potions[mid] * sp < success:
                    start = mid + 1
                else:
                    end = mid - 1
            if potions[mid] * sp >= success:
                res.append(len(potions) - mid)
            else:
                res.append(len(potions) - mid - 1)
            # print(mid - 1, potions[mid - 1]*sp)
            # res.append(len(potions) - 2 - (mid - 1))
        return res

if __name__ == '__main__':
    sol = Solution()
    spells = [40,11,24,28,40,22,26,38,28,10,31,16,10,37,13,21,9,22,21,18,34,2,40,40,6,16,9,14,14,15,37,15,32,4,27,20,24,12,26,39,32,39,20,19,22,33,2,22,9,18,12,5]
    potions = [31,40,29,19,27,16,25,8,33,25,36,21,7,27,40,24,18,26,32,25,22,21,38,22,37,34,15,36,21,22,37,14,31,20,36,27,28,32,21,26,33,37,27,39,19,36,20,23,25,39,40]
    success = 600

    # spells = [randint(1, 100000) for _ in range(100)]
    # potions = [randint(1, 100000) for _ in range(100)]
    # success = randint(1, 10000000000)

    # print(spells)
    # print(potions)
    # print(success)

    print(sol.successfulPairs(spells, potions, success))