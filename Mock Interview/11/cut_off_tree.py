'''
finished in last second
'''
class Solution:
    def cutOffTree(self, forest):
        m = len(forest)
        n = len(forest[0])
        if not self.can_cut(forest, m, n):
            # print('cant cut')
            return -1

        heights_with_location = []
        for x, row in enumerate(forest):
            for y, height in enumerate(row):
                if height > 1:
                    heights_with_location.append((height, x, y))
        heights_with_location = sorted(heights_with_location, key=lambda x:x[0])
        print(heights_with_location)

        res = 0
        prev_x = 0 
        prev_y = 0
        for _, x, y in heights_with_location:
            res += self.find_route(prev_x, prev_y, x, y, forest)
            print(res)
            prev_x = x
            prev_y = y
        return res
        
    def find_route(self, x, y, n_x, n_y, forest):
        directions = [(0,-1), (0,1), (-1,0),(1,0)]
        
        m = len(forest)
        n = len(forest[0])
        visited = [[0 for _ in range(n)] for __ in range(m)]
        visited[x][y] = 1
        q = [(x, y, 0)]
        while len(q) > 0:
            x, y, time = q[0]
            if x == n_x and y == n_y:
                return time
            for x_step, y_step in directions:
                x_next = x + x_step
                y_next = y + y_step
                if 0 <= x_next < m and 0 <= y_next < n:
                    if forest[x_next][y_next] > 0 and visited[x_next][y_next] == 0:
                        q.append((x_next, y_next, time+1))
                        visited[x_next][y_next] = 1
            q = q[1:]


    def all_cut(self, forest):
        for row in forest:
            for height in row:
                if height > 1:
                    return False
        return True

    def can_cut(self, forest, m, n):
        directions = [(0,-1), (0,1), (-1,0),(1,0)]
        visited = [[0 for _ in range(n)] for __ in range(m)]
        visited[0][0] = 1
        q = [(0,0)]
        while len(q) > 0:
            x, y = q[0]
            for x_step, y_step in directions:
                x_next = x + x_step
                y_next = y + y_step
                if 0 <= x_next < m and 0 <= y_next < n:
                    if forest[x_next][y_next] > 0 and visited[x_next][y_next] == 0:
                        q.append((x_next, y_next))
                        visited[x_next][y_next] = 1
            q = q[1:]

        for row_v, row_f in zip(visited, forest):
            for vis, height in zip(row_v, row_f):
                if vis == 0 and height > 0:
                    return False
        return True

if __name__ == '__main__':
    sol = Solution()
    forest = [
        [4557,6199,7461,2554,6132,7471,7103,4290],
        [2034,2301,6733,6040,2603,5697,9541,6678],
        [7308,7368,9618,4386,6944,3923,4754,4294],
        [0,3016,7242,5284,6631,1897,1767,7603],
        [2228,0,3625,7713,2956,3264,3371,6124],
        [9195,7804,2787,0,4919,9304,5161,502]
        ]
    print(sol.cutOffTree(forest))
        