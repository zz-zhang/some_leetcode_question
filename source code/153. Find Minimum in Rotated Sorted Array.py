from random import randint


class Solution:
    def findMin(self, nums):
        if len(nums) <= 2:
            if len(nums) == 1:
                return nums[0]
            else:
                return min(nums[0], nums[1])
        left = 0
        right = len(nums) - 1
        current = int(right / 2)
        # print(nums)
        while left < right:
            max_val = max(nums[left], nums[current], nums[right])
            min_val = min(nums[left], nums[current], nums[right])

            if min_val == nums[left] and max_val == nums[right]:
                break
            elif min_val == nums[left] and max_val == nums[current]:
                # print('error0')
                # print(left, current, right)
                break
            elif min_val == nums[current] and max_val == nums[right]:
                # print('error1')
                # print(left, current, right)
                break
            elif min_val == nums[current] and max_val == nums[left]:
                right = current
                current = int((left + right) / 2)
                # print(left, current, right)
                if right - left == 1:
                    return min(nums[left], nums[right])

            elif min_val == nums[right] and max_val == nums[left]:
                # print('error2')
                # print(left, current, right)
                break
            else:
                left = current
                current = int((left + right) / 2)
                # print(left, current, right)
                if right - left == 1:
                    return min(nums[left], nums[right])
        return nums[left]

if __name__ == '__main__':
    sol = Solution()
    nums = [i for i in range(3)]
    sum_res = 0
    for idx in range(5000):
        sum_res += sol.findMin(nums[idx:] + nums[:idx])
    print(sum_res)
        