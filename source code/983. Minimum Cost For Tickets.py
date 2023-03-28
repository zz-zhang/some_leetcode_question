from typing import List
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] + [1000000 for _ in days]
        times = [1, 7, 30]
        for idx, day in enumerate(days):
            # idx = idx + 1
            for cost, time in zip(costs[1:], times[1:]):
                last_covered_idx = idx
                while last_covered_idx > 0 and day - days[last_covered_idx] < time:
                    # print(day, days[last_covered_idx], time, day - days[last_covered_idx])
                    last_covered_idx -= 1
                if day - days[last_covered_idx] >= time:
                    last_covered_idx += 1

                # print(day, days[last_covered_idx], time)
                dp[idx+1] = min(dp[idx+1], dp[idx] + costs[0], dp[last_covered_idx] + cost)
                # print(days[last_covered_idx], day, time, dp[idx] + costs[0], dp[last_covered_idx] + cost, dp[idx+1])
            # print(dp)
        return dp[-1]



if __name__ == '__main__':
    sol = Solution()
    days = [1,4,6,7,8,20]
    costs = [2,7,15]
    print(sol.mincostTickets(days, costs))