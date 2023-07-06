class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {char: 0 for char in s}
        for char in s:
            dict_s[char] += 1
        

        for char in t:
            if char not in dict_s:
                return False
            if dict_s[char] < 1:
                return False
            dict_s[char] -= 1
        if sum(dict_s.values()) != 0:
            return False
        return True

if __name__ == '__main__':
    sol = Solution()
    s = "rat"
    t = "car"
    print(sol.isAnagram(s, t))