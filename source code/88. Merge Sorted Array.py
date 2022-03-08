from random import randint


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0 :
            return nums1
        
        i = 0
        j = 0
        tgt = m + n - 1
        while i < m or j < n:
            # print(i, j, tgt)
            if i < m and j < n:
                if nums1[i] <= nums2[j]:
                    nums1[tgt] = nums1[i]
                    i += 1
                else:
                    nums1[tgt] = nums2[j]
                    j += 1
            elif i < m:
                nums1[tgt] = nums1[i]
                i += 1
            else:
                nums1[tgt] = nums2[j]
                j += 1
            
            if tgt > m:
                tgt -= 1
            elif tgt == m:
                tgt = 0
            else:
                tgt += 1
        # print(nums1)
        for idx in range(int(m / 2)):
            nums1[idx], nums1[m-idx-1] = nums1[m-idx-1], nums1[idx]
        for idx in range(int((m + n) / 2)):
            nums1[idx], nums1[m+n-idx-1] = nums1[m+n-idx-1], nums1[idx]

if __name__ == '__main__':
    sol = Solution()
    import random
    m = 200
    n = 200 - m
    nums1 = sorted([randint(-10000, 10000) for _ in range(m)]) + [0 for _ in range(n)]
    nums2 = sorted([randint(-10000, 10000) for _ in range(n)])

    print(nums1)
    print(m)
    print(nums2)
    print(n)

    sol.merge(nums1, m, nums2, n)
    print(nums1)