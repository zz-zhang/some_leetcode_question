class Solution:
    def exist(self, s, t):
        if len(s) < len(t):
             return False
        for i in t:
            if i not in s:
                return False
        return True

    def findOver(self, used, aim):
        for i in used:
            if used[i] < aim[i]:
                return False
        return True

    def findEnd(self, s, t, begin):
        used = {}
        aim = {}
        for i in t:
            used[i] = 0
            aim[i] = 0
        for i in t:
            aim[i] += 1

        used[s[begin]] = 1
        for i in range(begin, len(s)):
            if s[i] in t:
                if i != begin and used[s[i]] == aim[s[i]]:
                    return 0xFFFF
                else:
                    used[s[i]] += 1
            if self.findOver(used, aim):
                return i
        return 0xFFFF

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        if not self.exist(s, t):
            return ""
        begin = 0
        end = len(s) - 1
        length = len(s) + 1
        for i in range(0, len(s)):
            if s[i] in t:
                j = self.findEnd(s, t, i)
                if j - i < length:
                    length = j - i
                    begin = i
                    end = j
        res = s[begin : end + 1]
        return res



if __name__ == '__main__':
    sol = Solution()
    s = "aa"
    t = "aa"
    print(sol.minWindow(s, t))