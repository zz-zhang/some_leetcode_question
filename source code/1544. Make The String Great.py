class Solution:
    def makeGood(self, s):
        good, flags = self.isGood(s)
        new_s = ''
        while not good:
            # print(s, flags)
            for flag, char in zip(flags, s):
                if flag == 0:
                    new_s = new_s + char
            s = new_s
            new_s = ''
            good, flags = self.isGood(s)
        return s
    
    def isGood(self, s):
        flags = [0 for _ in range(len(s))]
        for idx, (c1, c2) in enumerate(zip(s[:-1], s[1:])):
            if c1.lower() == c2.lower() and c1 != c2:
                flags[idx] += 1
                flags[idx + 1] += 1
        
        for idx, flag in enumerate(flags):
            if flag == 2:
                flags[idx + 1] -=1

        if sum(flags) == 0:
            return True, flags
        else:
            return False, flags

if __name__ == '__main__':
    sol = Solution()
    s = "aAAaa" * 20

    print(sol.makeGood(s))