'''
An axis-aligned rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) is the coordinate of its bottom-left corner, and (x2, y2) is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.

Two rectangles overlap if the area of their intersection is positive. To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two axis-aligned rectangles rec1 and rec2, return true if they overlap, otherwise return false.
'''

class Solution:
    def isRectangleOverlap(self, rec1, rec2) :
        x11, y11, x12, y12 = rec1
        x21, y21, x22, y22 = rec2
        # R1 or R2 no exist
        if x11 == x12 or y11 == y12 or x21 == x22 or y21 == y22:
            return False
        # breakpoint()
        # R2 on the left
        if y22 <= y11:
            return False
        # R2 on the right
        if y21 >= y12:
            return False

        # R2 on the top
        if x21 >= x12:
            return False
        # R2 on the bottom
        if x22 <= x11:
            return False

        return True

if __name__ == '__main__':
    sol = Solution()
    rec1 = [7,8,13,15]
    rec2 = [10,8,12,20]
    print(sol.isRectangleOverlap(rec2, rec1))
