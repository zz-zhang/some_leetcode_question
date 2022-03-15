class Solution:
    def minRemoveToMakeValid(self, s: str):
        counter = [0 for _ in range(len(s))]
        stack = 0
        idx_recoder = []
        for idx, char in enumerate(s):
            if char == '(':
                stack += 1
            if char == ')':
                if stack > 0:
                    stack -= 1
                else:
                    idx_recoder.append(idx)
                    stack = 0
        res = [char for idx, char in enumerate(s) if idx not in idx_recoder]
        # print(''.join(res))
        while stack > 0:
            for idx in range(len(res) - 1, -1, -1):
                if res[idx] == '(':
                    res = res[:idx] + res[idx+1:]
                    stack -= 1
                    break
        # print(''.join(res))
        return ''.join(res)

if __name__ == '__main__':
    sol = Solution()
    s = "))(()"
    print(sol.minRemoveToMakeValid(s))