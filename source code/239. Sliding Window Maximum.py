from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = []

        for q_idx in range(0, k):
            queue = self.add_to_decreasing_queue(queue, nums[q_idx])
        print(queue)

        res = [max(queue)]
        for idx in range(k, len(nums)):
            # breakpoint()
            if nums[idx - k] == queue[0]:
                queue.pop(0)
            queue = self.add_to_decreasing_queue(queue, nums[idx])
            res.append(queue[0])
            # print(queue)
        return res

    def add_to_decreasing_queue(self, queue, item):
        if len(queue) == 0:
            queue.append(item)
            return queue
        while len(queue) > 0 and queue[-1] < item:
            queue.pop(-1)
        queue.append(item)
        return queue


if __name__ == '__main__':
    sol = Solution()
    nums = [-1, 1]
    k = 1
    print(sol.maxSlidingWindow(nums, k))