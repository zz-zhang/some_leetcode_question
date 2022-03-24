from random import randint
from typing import *

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        # print(people)
        res = 0
        i = 0
        j = len(people) - 1
        while i <= j:
            res += 1
            if people[j] == limit:
                j -= 1
            elif people[i] + people[j] <= limit:
                i += 1
                j -= 1
            else:
                j -= 1
        # print(res)
        return res


if __name__ == '__main__':
    sol = Solution()
    people = [3,5,3,4]
    limit = 3 * 10 ** 4
    people = [randint(1, limit) for _ in range(1000)]
    print(people)
    sol.numRescueBoats(people, limit)