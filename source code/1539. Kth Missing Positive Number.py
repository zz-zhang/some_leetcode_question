from typing import List
import random

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        curr = 1
        p = 0

        while k > 0:
            if p < len(arr):
                if curr == arr[p]:
                    curr += 1
                    p += 1
                elif curr < arr[p]:
                    k -= 1
                    if k == 0:
                        break
                    curr += 1
                else:
                    k -= 1
                    if k == 0:
                        break
                    curr += 1
            else:
                k -= 1
                if k == 0:
                    break
                curr += 1

        return curr

if __name__ == '__main__':
    sol = Solution()
    # arr = [2,3,4,7,11]
    # k = 7
    arr = random.sample([i for i in range(1, 1001)], 990)
    k = 19
    print(sol.findKthPositive(arr, k))
