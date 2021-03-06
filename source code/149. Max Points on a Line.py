class Solution:
    def gcd(self, x, y):
        if x == y:
            return x
        # elif x < y:
        #     return self.gcd(x, y - x)
        # else:
        #     return self.gcd(x - y, y)
        while x != y:
            if x > y:
                x, y = x - y, y
            else:
                x, y = x, y - x
        return x

    def fraction_reduction(self, x, y):
        flag_x, flag_y = 1, 1
        if x < 0 and y < 0:
            x = -x
            y = -y
        elif x < 0:
            flag_x = -1
            x = -x
        elif y < 0:
            flag_y = -1
            y = -y
        if x == 0 or y == 0 or x == 1 or y == 1:
            return x * flag_x, y * flag_y
        gcd = self.gcd(x, y)
        return int(flag_x * x / gcd), int(flag_y * y / gcd)

    def maxPoints(self, points) -> int:
        if len(points) <= 2:
            return len(points)
        slope = {}
        for i in range(0, len(points)):
            for j in range(i + 1, len(points)):
                (x1, y1) = points[i]
                (x2, y2) = points[j]
                dx, dy = self.fraction_reduction(x1 - x2, y1 - y2)
                if (dx, dy) not in slope:
                    slope[(dx, dy)] = [(x1, y1), (x2, y2)]
                else:
                    if (x1, y1) not in slope[(dx, dy)]:
                        slope[((dx, dy))] += [(x1, y1)]
                    if (x2, y2) not in slope[(dx, dy)]:
                        slope[((dx, dy))] += [(x2, y2)]

        result = 0
        for point in slope:
            result = max(result, len(slope[point]))
        return result

if __name__ == '__main__':
    sol = Solution()
    # points = [[1, 1], [2, 2], [3, 3]]
    # points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    points = [[0,0],[1,65536],[65536,0]]
    print(sol.maxPoints(points))