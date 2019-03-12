class Solution:
    def findMax(self, height):
        i = 0
        loc = 0
        maxHeight = 0
        while i < len(height):
            if maxHeight < height[i]:
                maxHeight = height[i]
                loc = i
            i += 1
        return loc

    def findEnd(self, height, lstart, rstart):
        lend = self.findMax(height[:lstart])
        if rstart + 1 < len(height):
            rend = self.findMax(height[rstart + 1: ]) + rstart + 1
        else:
            rend = rstart
        return lend, rend

    def calcCap(self, height, start, end):
        wall = height[end]
        if start > end:
            start = start + end
            end = start - end
            start = start - end

        res = 0
        for i in range(start + 1, end):
            res += wall - height[i]
        return res

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0:
            return 0
        lstart = rstart = 0
        lend = rend = 0
        lstart = rstart = self.findMax(height)
        res = 0
        while True:
            lend, rend = self.findEnd(height, lstart, rstart)
            res += self.calcCap(height, lstart, lend)
            res += self.calcCap(height, rstart, rend)
            lstart = lend
            rstart = rend
            if lstart == 0 and rstart == len(height) - 1:
                break
        return res

if __name__ == '__main__':
    sol = Solution()
    height =  [0, 0, 1, 2, 0, 1]
    print(sol.trap(height))