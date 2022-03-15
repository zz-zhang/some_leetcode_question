'''
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.
'''
class Solution:
    def countCharacters(self, words, chars):
        res = 0
        chars_count = {char:0 for char in chars}
        for char in chars:
            chars_count[char] += 1
        # print(chars_count)
        for word in words:
            word_count = {char:0 for char in word}
            temp_chars_count = {k: v for k, v in chars_count.items()}
            for char in word:
                word_count[char] += 1
            # print(word_count)
            for char, num in word_count.items():
                if char not in temp_chars_count or num > temp_chars_count[char]:
                    break
                else:
                    temp_chars_count[char] -= 1
            else:
                res += len(word)
        return res
        
if __name__ == '__main__':
    sol = Solution()
    words = ["hello","world","leetcode"]
    chars = "welldonehoneyr"
    print(sol.countCharacters(words, chars))