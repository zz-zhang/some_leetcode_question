class Solution:
    def divide(self, dividend, divisor):
        res = [0 for _ in range(0, divisor)]
        while dividend > 0:
            for index in range(0, min(dividend, divisor)):
                res[index] += 1
            dividend -= divisor
        return res

    def add_space(self, raw_words, maxWidth, is_last_line = False):
        res = ''
        word_list = raw_words.split()
        if not is_last_line and len(word_list) != 1:

            word_len = sum([len(item) for item in word_list])
            space_list = self.divide(maxWidth - word_len, len(word_list) - 1)
            for index in range(0, len(space_list)):
                res += word_list[index] + ' ' * space_list[index]
            res += word_list[-1]
        else:
            res = raw_words
            while len(res) < maxWidth:
                res += ' '
        return res

    def fullJustify(self, words, maxWidth):
        res = []
        index = 0
        temp_res = ''
        while index < len(words):
            if len(temp_res) == 0:
                temp_res = words[index]
                index += 1
                if index == len(words):
                    res.append(self.add_space(temp_res, maxWidth, is_last_line=True))
                continue
            if len(temp_res) + 1 + len(words[index]) <= maxWidth:
                temp_res = temp_res + ' ' + words[index]
                index += 1
                if index == len(words):
                    res.append(self.add_space(temp_res, maxWidth, is_last_line=True))
            else:
                res.append(self.add_space(temp_res, maxWidth))
                temp_res = []
        # for item in res:
        #     print(item + '|')
        return res

if __name__ == '__main__':
    s = Solution()
    words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
    maxWidth = 20
    print(s.fullJustify(words, maxWidth))