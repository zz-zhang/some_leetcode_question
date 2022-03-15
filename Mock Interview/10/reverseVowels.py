class Solution:
    def reverseVowels(self, s: str):
        s = list(s)
        i = 0
        j = len(s) - 1
        while i < j:
            while i <= j and s[i] not in 'aeiouAEIOU':
                i += 1
            while i <= j and s[j] not in 'aeiouAEIOU':
                j -= 1

            if i <= j and s[i] in 'aeiouAEIOU' and s[j] in 'aeiouAEIOU':
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return ''.join(s)
        
if __name__ == '__main__':
    sol = Solution()
    s = "qwrt"
    print(sol.reverseVowels(s))