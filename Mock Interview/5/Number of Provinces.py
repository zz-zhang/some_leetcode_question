'''
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
'''

class Solution:
    def findCircleNum(self, isConnected):
        res = 0
        colored = [0 for _ in range(len(isConnected))]
        for city in range(len(isConnected)):
            q = [city]
            if colored[city] == 0:
                res += 1
                colored[city] = res
            while len(q) > 0:
                currect_city = q[0]
                if colored[currect_city] == 0:
                    colored[currect_city] = colored[city]
                
                for idx, connect in enumerate(isConnected[currect_city]):
                    if connect == 1 and colored[idx] == 0:
                        q.append(idx)
                q = q[1:]
        return res

if __name__ == '__main__':
    sol = Solution()
    isConnected = [[1,1,1],[1,1,1],[1,1,1]]
    print(sol.findCircleNum(isConnected))