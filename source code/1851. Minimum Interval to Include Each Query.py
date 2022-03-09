from random import randint


class Solution:
    def minInterval(self, intervals, queries):
        duration = {}
        for (l, r) in intervals:
            if (r - l + 1) not in duration:
                duration[(r - l + 1)] = [(l, r)]
            else:
                duration[(r - l + 1)].append((l, r))
        # print(start_with)
    
        keys = sorted(duration.keys())

        res = []
        for idx, q in enumerate(queries):
            res.append(self.find(duration, keys, q))
            
                
        # res = [r if r < 1e7+1 else -1 for r in res]
        return res

    def find(self, duration, keys, query):
        for dura in keys:
            for l, r in duration[dura]:
                if l <= query <= r:
                    return dura
        return -1

if __name__ == '__main__':
    sol = Solution()
    intervals = [[2,3],[2,5],[1,8],[20,25]]
    queries = [2,19,5,22]

    intervals = []
    for _ in range(100000):
        a = randint(1, 10000000)
        b = randint(1, 10000000)
        if a > b:
            a, b = b, a
        intervals.append([a, b])
    queries = [randint(1, 1000000) for _ in range(10000)]
    print(sol.minInterval(intervals, queries))