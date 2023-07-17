from typing import List
from random import randint, choice

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0
        intervals = sorted(intervals, key=lambda x: (x[1], x[0]))
        # print(intervals)
        idx = 1
        num_unoverlap = 1
        last_end = intervals[0][1]
        # print(intervals[0])
        while idx < len(intervals):
            s, e = intervals[idx]
            if s >= last_end:
                last_end = e
                num_unoverlap += 1
                # print(s, e)
            idx += 1
        return len(intervals) - num_unoverlap


if __name__ == '__main__':
    sol = Solution()
    intervals = [[1,2],[2,3]]
    print(intervals)
    print(sol.eraseOverlapIntervals(intervals))