class Solution:
    def isNumber(self, s: str) -> bool:
        import re
        int_pattern = r'[+|-]?[0-9]+'
        float_pattern_1 = r'[+|-]?[0-9]*\.[0-9]+'
        float_pattern_2 = r'[+|-]?[0-9]+\.[0-9]*'
        exponent_pattern_1 = r'[+|-]?[0-9]+e[+|-]?[0-9]+'
        exponent_pattern_2_1 = r'[+|-]?[0-9]*\.[0-9]+e[+|-]?[0-9]+'
        exponent_pattern_2_2 = r'[+|-]?[0-9]+\.[0-9]*e[+|-]?[0-9]+'
        pattern = [int_pattern, float_pattern_1, float_pattern_2, exponent_pattern_1, exponent_pattern_2_1, exponent_pattern_2_2]
        s = s.split()
        if len(s) != 1:
            return False
        s = s[0]
        for pt in pattern:
            if re.match(pt, s) is not None and re.match(pt, s).span() == (0, len(s)):
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    input_str = " .1"
    print(s.isNumber(input_str))