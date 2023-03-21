from typing import List
import random

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        '''
            suppose we want a T times to finish the trip, and each bus time[i] will finish 1/time[i] trip.
            so the target is to make sum([T/time[0], T/time[1], ..., T/time[n]]) >= totalTrips,
            which can transform to T*sum(1/time) >= totalTrips,
            T*sum(time) >= totalTrips*lcm(time)
            T >= totalTrips*lcm(time)/sum()time
            Note: use cm but not lcm to save time
        '''
        # def mlp(nums):
        #     res = 1
        #     for num in nums:
        #         res = res * num
        #         # print(res)
        #     return res
        import math
        # cm = math.lcm(*time)
        # # cm = mlp(time)
        # # print(cm)
        # res = totalTrips * cm / sum([int(cm / t) for t in time])
        # # res = res * cm
        # # print(res)
        # res = math.ceil(res)
        # # print(res)
        # return res
        start_num = 
        

if __name__ == '__main__':
    sol = Solution()
    time = [2,3,5]
    totalTrips = 5
    # time = [random.randint(1, 1000) for _ in range(100)]
    # totalTrips = 10000000
    print(time)
    print(sol.minimumTime(time, totalTrips))