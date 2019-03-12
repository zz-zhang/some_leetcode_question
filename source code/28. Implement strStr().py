class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        if needle in haystack:
            i = 0
            while True:
                if haystack[:len(needle)] == needle:
                    return i
                haystack = haystack[1:]
                i += 1
        else:
            return -1

if __name__ == '__main__':
    sol = Solution()
    haystack = 'bba'
    needle = 'a'
    print(sol.strStr(haystack, needle))
