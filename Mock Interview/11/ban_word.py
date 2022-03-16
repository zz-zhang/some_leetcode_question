class Solution:
    def mostCommonWord(self, paragraph, banned):
        import re
        split_pattern = r' |\!|\?|\'|\,|\;|\.'
        paragraph = paragraph.lower()
        words = re.split(split_pattern, paragraph)
        words = [word for word in words if len(word) > 0]
        # print(words)
        counter = {}
        for word in words:
            if word in counter:
                counter[word] += 1
            else:
                counter[word] = 1

        max_count = -1
        target_word = ''
        for word, number in counter.items():
            if word not in banned:
                if number > max_count:
                    max_count = number
                    target_word = word
        return target_word

if __name__ == '__main__':
    sol = Solution()
    paragraph = "."
    banned = [""]
    print(sol.mostCommonWord(paragraph, banned))
        