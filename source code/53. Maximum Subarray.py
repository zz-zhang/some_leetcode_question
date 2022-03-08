import random

class Solution:
    def maxSubArray(self, nums):
        non_neg = [num for num in nums if num >= 0]
        if len(non_neg) == 0:
            return max(nums)

        # nums = self.group(nums)
        sub_res = 0
        res = 0
        for num in nums:
            sub_res = max(sub_res + num, 0)
            res = max(sub_res, res)
        return res

    # def sumTriple(self, nums):
    #     if len(nums) == 3:
    #         res = max(nums[0], nums[1], sum(nums))
    #         if res == nums[0]:
    #             return res, False
    #         else:
    #             return res, True
    #     else:
    #         prev, contious = self.sumTriple(nums[:-2])
    #         if contious:
    #             res = max(prev, nums[-1], prev + nums[-2] + nums[-1])
    #         else:
    #             res = max(prev, nums[-1])
    #         if res == prev:
    #             return res, False
    #         else:
    #             return res, True

    # def group(self, nums):
    #     grouped = []
    #     sub_res = nums[0]
    #     factor = 1 if nums[0] >= 0 else -1
    #     for num in nums[1:]:
    #         if (num > 0 and factor > 0) or (num < 0 and factor < 0):
    #             sub_res = sub_res + num
    #         else:
    #             grouped.append(sub_res)
    #             sub_res = num
    #             factor = factor * -1
    #     else:
    #         grouped.append(sub_res)
    #     if grouped[0] < 0:
    #         grouped = grouped[1:]
    #     if grouped[-1] < 0:
    #         grouped = grouped[:-1]
    #     # print(grouped)
    #     return grouped


    # def divide(self, nums, depth=0):
    #     if len(nums) == 1:
    #         return nums[0]
    #     res = -1e5
    #     print(depth)
    #     for idx, num in enumerate(nums):
    #         if num < 0:
    #             if nums[idx - 1] + num < 0 or nums[idx + 1] + num < 0:
    #                 sum1 = sum(nums[:idx])
    #                 sum2 = sum(nums[idx+1:])
    #                 sub_res = max(self.divide(nums[:idx], depth+1), self.divide(nums[idx+1:], depth+1), sum1, sum2)
    #                 if sub_res > res:
    #                     res = sub_res
    #     return res
        # print(sum1, nums1)
        # print(sum2, nums2)


        # return max(self.divide(nums1), self.divide(nums2), sum1, sum2)
        # if sum1 > sum2:
        #     if len(nums1) == 1:
        #         return sum1
        #     return max(self.divide(nums1), sum1)
        # else:
        #     if len(nums2) == 1:
        #         return sum2
        #     return max(self.divide(nums2), sum2)
 

if __name__ == '__main__':
    sol = Solution()
    nums = [random.randint(-1000, 1000) for _ in range(50)]
    print(nums)
    print(sol.maxSubArray(nums))
        