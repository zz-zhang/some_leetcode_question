from typing import List
import sys

sys.setrecursionlimit(2001)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # circle finding by dfs
        self.sons = [set() for n in range(numCourses)]

        for course, requirement in prerequisites:
            self.sons[requirement].add(course)
        
        self.checked = set()

        for n in range(numCourses):
            if n not in self.checked:
                if not self.dfs(n, []):
                    return False
            # print(self.checked)
            # breakpoint()
        return True

    def dfs(self, node, visited):
        if node in visited:
            # print(f'find loop at {node}')
            return False
        for son in self.sons[node]:
            if son not in self.checked:
                if not self.dfs(son, visited + [node]):
                    return False
                self.checked.add(son)

        return True

if __name__ == '__main__':
    sol = Solution()
    numCourses = 2
    prerequisites = [[0,1], [1,0]]

    print(sol.canFinish(numCourses, prerequisites))
