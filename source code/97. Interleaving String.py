class Solution:
    def isInterleave(self, s1, s2, s3):
        if s1 + s2 == s3 or s2 + s1 == s3:
            return True
        p1 = 0
        p2 = 0
        for p3 in range(len(s3)):
            if (p1 < len(s1) and s3[p3] == s1[p1]) or (p2 < len(s2) and s3[p3] == s2[p2]):
                if p1 < len(s1) and p2 < len(s2) and s1[p1] == s2[p2]:
                    if self.isInterleave(s1[p1 + 1:], s2[p2:], s3[p3 + 1:]):
                        return True
                    elif self.isInterleave(s1[p1:], s2[p2 + 1:], s3[p3 + 1:]):
                        return True
                    else:
                        return False
                elif p1 < len(s1) and s1[p1] == s3[p3]:
                    p1 += 1
                elif p2 < len(s2) and s2[p2] == s3[p3]:
                    p2 += 1
                else:
                    return False
            else:
                return False
        if p1 == len(s1) and p2 == len(s2):
            return True
        return False

if __name__ == '__main__':
    sol = Solution()
    s1 = "ab"
    s2 = "c"
    s3 = "c"
    print(sol.isInterleave(s1, s2, s3))
