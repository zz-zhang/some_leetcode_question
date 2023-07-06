class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict_m = {char: 0 for char in magazine}
        for char in magazine:
            dict_m[char] += 1
        

        for char in ransomNote:
            if char not in dict_m:
                return False
            if dict_m[char] < 1:
                return False
            dict_m[char] -= 1
        return True
        

if __name__ == '__main__':
    sol = Solution()
    ransomNote = "aa"
    magazine = "ba"
    print(sol.canConstruct(ransomNote, magazine))