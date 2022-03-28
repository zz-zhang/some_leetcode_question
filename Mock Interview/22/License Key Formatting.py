class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.upper()
        s = s.replace('-', '')
        mod = len(s) % k
        # print(s, len(s), mod)
        res = s[:mod]
        s = s[mod:]
        for i in range(0, len(s), k):
            res = res + '-' + s[i: i + k]
        if len(res) > 0 and res[0] == '-':
            res = res[1:]
        return res

if __name__ == '__main__':
    sol = Solution()
    s = "---"
    k = 3
    print(sol.licenseKeyFormatting(s, k))