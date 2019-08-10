import sys
sys.setrecursionlimit(10000000)

class Solution:
    def largestRectangleArea(self, heights) -> int:

        # TLE method
        # ---------------------------------------------
        # maxRec = 0
        # for index, item in enumerate(heights):
        #     start_flag, end_flag = 0, 0
        #     for start in range(index, -1, -1):
        #         if heights[start] >= item:
        #             start_flag = start
        #         else:
        #             break
        #     for end in range(index, len(heights)):
        #         if heights[end] >= item:
        #             end_flag = end
        #         else:
        #             break
        #     maxRec = max(maxRec, item * (end_flag - start_flag + 1))
        # return maxRec
        # ---------------------------------------------


        # TLE method2
        # ---------------------------------------------
        # min_height_list = {height:[] for height in heights}
        # for index, item in enumerate(heights):
        #     for height in min_height_list:
        #         if height <= item:
        #             min_height_list[height] += [index]
        #
        # maxRec = 0
        # for key in min_height_list:
        #     maxRec = max(maxRec, key * self.max_continue_length(min_height_list[key]))
        # return maxRec
        # ---------------------------------------------


        left = [1] * len(heights)
        right = [1] * len(heights)
        for i in range(0, len(heights)):
            j = i - 1
            while j >= 0:
                if heights[j] >= heights[i]:
                    left[i] += left[j]
                    j -= left[j]
                else:
                    break

        for i in range(len(heights) - 1, 0 - 1, -1):
            j = i + 1
            while j < len(heights):
                if heights[j] >= heights[i]:
                    right[i] += right[j]
                    j += right[j]
                else:
                    break
        result = 0
        for i in range(0, len(heights)):
            area = (right[i] + left[i] - 1) * heights[i]
            result = area if area > result else result
        return result



if __name__ == '__main__':
    sol = Solution()
    heights =[2,1,5,6,2,3]
        # ,97586333,68834337,62979669,1783127,29339118,83907628,48067922
        # ,22843915,11027247,73603247,32376863,12448072,7086475,2369889
        # ,5064817,88893600,61558880,77108330,32113014,21324782,28294417
        # ,18403046,39022240,58687324,80978280,584748,76209754,25165237
        # ,40959391,6378795,66709524,38545724,75213133,29689193,92845203
        # ,4552251,13596821,40913125,27396166,24624068,67032725,12289382
        # ,89588493,74119200,14659271,94653310,15529152,28734503,24277993]
    print(sol.largestRectangleArea(heights))