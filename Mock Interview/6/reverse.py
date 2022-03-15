'''
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.
'''
class Solution:
    def reverseStr(self, s: str, k: int):
        reverse = True
        s = list(s)
        for idx in range(0, len(s), k):
            # print(idx)
            if reverse:
                left = idx
                right = len(s) - 1 if idx + k >= len(s) else idx + k - 1
                self.reverse_str(s, left, right)
            reverse = not reverse
        return ''.join(s)
    
    def reverse_str(self, s, left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        # print(s)

if __name__ == "__main__": 
    sol = Solution()
    s = "a"
    k = 1
    print(sol.reverseStr(s, k))