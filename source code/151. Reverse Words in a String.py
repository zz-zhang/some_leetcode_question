class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        res1 = []
        res2 = []
        # print(words)
        left, right = 0, len(words) - 1
        while left <= right:
            while len(words[left]) == 0 and left < right:
                left += 1
            while len(words[right]) == 0 and left < right:
                right -= 1
            res1.append(words[right])
            if left != right:
                res2.append(words[left])
            left += 1
            right -= 1

        # print(res1, res2)
        return ' '.join(res1+res2[::-1])

if __name__ == '__main__':
    sol = Solution()
    s = " "
    print(sol.reverseWords(s))