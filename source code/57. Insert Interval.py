# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        if len(intervals) == 0:
            return [newInterval]
        start = newInterval.start
        end = newInterval.end
        for item in intervals:
            if start < item.start:
                pass
            elif start <= item.end:
                start = item.start

            if end > item.end:
                pass
            elif end >= item.start:
                end = item.end
        # print(start, end)
        res = []
        appended = False

        if end < intervals[0].start:
            res.append(Interval(start, end))

        for item, item2 in zip(intervals + [None], [None] + intervals):
            if item is None:
                continue

            if item2 is not None:
                if item2.end < start and item.start > end and not appended:
                    res.append(Interval(start, end))
                    appended = True

            if item.start < start or item.end > end:
                res.append(item)
            elif not appended:
                res.append(Interval(start, end))
                appended = True

        if start > intervals[-1].end:
            res.append(Interval(start, end))

        # for item in res:
        #     print(item.start, item.end)
        return res

if __name__ == '__main__':
    s = Solution()
    input_list = [[3,5],[12,15]]
    input_interval_list = []
    new_interval = Interval(16, 18)
    for item in input_list:
        input_interval_list.append(Interval(item[0], item[1]))
    print(s.insert(input_interval_list, new_interval))
