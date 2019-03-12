class Solution:
    def isValid(self, S: str) -> bool:
        if S[0] != 'a' or S[-1] != 'c':
            return False
        prev_length = len(S)
        while True:
            S = S.replace('abc', '')
            length = len(S)
            if length == 0:
                return True
            if length == prev_length:
                return False
            prev_length = length

if __name__ == '__main__':
    s = Solution()
    input = "aabcbabcc"
    print(s.isValid(input))