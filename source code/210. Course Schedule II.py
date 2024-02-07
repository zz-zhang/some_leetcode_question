from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        requirements = [set() for i in range(numCourses)]
        followings = [set() for i in range(numCourses)]

        for course, requirement in prerequisites:
            requirements[course].add(requirement)
            followings[requirement].add(course)
        
        # print(requirements)
        # print(followings)

        q = [idx for idx, req in enumerate(requirements) if not req]
        # visited = set()
        taken = set()
        res = []
        while q:
            course = q.pop(0)
            # visited.add(course)
            if requirements[course].issubset(taken) and course not in taken:
                taken.add(course)
                res.append(course)

                for following_course in followings[course]:
                    if following_course not in taken:
                        q.append(following_course)
            # print(q)
        # res = 0
        print(res)
        return res if len(res) == numCourses else []



if __name__ == '__main__':
    sol = Solution()
    numCourses = 3
    prerequisites = [[0,1], [0,2], [1,2]]
    print(sol.findOrder(numCourses, prerequisites))