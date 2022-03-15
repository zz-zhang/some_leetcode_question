class Solution:
    def countSubstrings(self, s):
        res = {}
        for length in range(1, len(s) + 1):
            for idx in range(0, len(s)):
                if idx + length <= len(s):
                    sub_str = s[idx: idx + length]
                    if sub_str in res.keys():
                        res[sub_str] += 1
                    elif self.is_palindromic(sub_str): 
                        # print(idx, length, sub_str)
                        res[sub_str] = 1
        # print(res)
        return sum(res.values())
    
    def is_palindromic(self, s):
        if len(s) == 1:
            return True

        head = 0
        tail = len(s) - 1
        while head <= tail:
            if s[head] != s[tail]:
                return False
            head += 1
            tail -= 1
        return True
    

if __name__ == '__main__':
    sol = Solution()
    s = 'a' * 1000
    print(sol.countSubstrings(s))
        