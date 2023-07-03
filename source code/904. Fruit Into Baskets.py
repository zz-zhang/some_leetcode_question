from typing import List
from random import randint

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        picked = set()
        picked_counter = {t: 0 for t in fruits}

        left, right = 0, 0
        res = 0
        while right < len(fruits):
            if len(picked) < 2:
                picked.add(fruits[right])
                picked_counter[fruits[right]] += 1
            else:
                if fruits[right] in picked:
                    picked_counter[fruits[right]] += 1
                else:
                    while len(picked) == 2:
                        picked_counter[fruits[left]] -= 1
                        if picked_counter[fruits[left]] == 0:
                            picked.remove(fruits[left])
                        left += 1

                    picked.add(fruits[right])
                    picked_counter[fruits[right]] += 1

            res = max(res, right - left + 1)
            right += 1
        return res

        
if __name__ == '__main__':
    sol = Solution()
    fruits = [1,2,3,2,2]
    fruits = [randint(1, int(1000)) for _ in range(1000)]
    print(fruits)
    print(sol.totalFruit(fruits))