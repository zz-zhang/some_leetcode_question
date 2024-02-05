from typing import List
from random import randint, choice, sample

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1
        while start != end:
            res = numbers[start] + numbers[end]
            if res == target:
                return [start + 1, end + 1]
            if res < target:
                start += 1
            if res > target:
                end -= 1


if __name__ == '__main__':
    sol = Solution()
    numbers = [-1, 0]
    target = -1
    numbers = sample(range(-1000, 1001), 2000)
    numbers.sort()
    target = choice(numbers) + choice(numbers)
    print(numbers)
    print(target)
    print(sol.twoSum(numbers, target))