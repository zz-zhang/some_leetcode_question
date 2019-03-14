# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def take_start(interval):
    return (interval.start, interval.end)

class Solution:
    def merge_able(self, interval_1, interval_2):
        if interval_1.start > interval_2.start:
            interval_1, interval_2 = interval_2, interval_1
        if interval_1.end >= interval_2.start:
            return interval_1.start, max(interval_1.end, interval_2.end)
        return None, None

    def merge(self, intervals):
        if len(intervals) == 0:
            return []
        if len(intervals) == 1:
            return intervals
        index = 1
        intervals.sort(key=take_start)
        # for item in intervals:
        #     print(item.start, item.end)
        while index < len(intervals):
            if index == len(intervals):
                break
            new_start, new_end = self.merge_able(intervals[index - 1], intervals[index])
            if new_start is not None:
                new_interval = Interval(new_start, new_end)
                intervals.pop(index - 1)
                intervals[index - 1] = new_interval
            else:
                index += 1
        # for item in intervals:
        #     print(item.start, item.end)
        return intervals


if __name__ == '__main__':
    s = Solution()
    input_list = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
    input_interval_list = []
    # new_interval = Interval(16, 18)
    for item in input_list:
        input_interval_list.append(Interval(item[0], item[1]))
    print(s.merge(input_interval_list))
