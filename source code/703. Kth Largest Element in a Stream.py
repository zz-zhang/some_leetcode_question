from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums, reverse=True)[:self.k]
        # self.res = self.nums[k - 1]

    def add(self, val: int) -> int:
        if len(self.nums) >= self.k and val < self.nums[-1]:
            return self.nums[-1]
        else:
            self.nums = sorted(self.nums + [val], reverse=True)[:self.k]
            return self.nums[-1]



if __name__ == '__main__':
    obj = KthLargest(10 ** 4, [4, 5, 8, 2])
    for i in range(10 ** 4):
        print(obj.add(i))
