import random
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        p1, p2 = 0, 0
        while p2 < len(nums2):
            while p1 < len(nums1) and nums1[p1] < nums2[p2]:
                p1 += 1
            if p1 == len(nums1):
                nums1 = nums1 + [nums2[p2]]
            else:
                nums1 = nums1[:p1] + [nums2[p2]] + nums1[p1:]
            p2 += 1
        # print(nums1)

        if len(nums1) % 2 == 0:
            return (nums1[int(len(nums1) / 2) - 1] + nums1[int(len(nums1) / 2)]) / 2
        else:
            return nums1[int(len(nums1) / 2)]

if __name__ == '__main__':
    sol = Solution()
    nums1 = [1, 3]
    nums2 = [2, 3]
    nums1 = sorted([random.randint(int(10e5)*-1, int(10e5)) for _ in range(1000)])
    nums2 = sorted([random.randint(int(10e5)*-1, int(10e5)) for _ in range(1000)])
    
    print(nums1)

    print(nums2)

    print(sol.findMedianSortedArrays(nums1, nums2))
