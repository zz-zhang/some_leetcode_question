class Solution:
    def firstMissingPositive(self, nums):
        positive_num = [item for item in nums if item > 0]
        pos_num_length = len(positive_num)
        limit_num = [item for item in positive_num if item <= pos_num_length]
        # if 1 not in new_num:
        #     return 1
        # length_sum = sum([item for item in range(0, pos_num_length + 1)])
        res = 1
        while len(limit_num) > 0:
            if res in limit_num:
                limit_num.remove(res)
                res += 1
            else:
                return res
        return res

if __name__ == '__main__':
    s = Solution()
    nums = [3,2,-1,1]
    print(s.firstMissingPositive(nums))