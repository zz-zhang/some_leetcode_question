class Solution:
    def findSubstring(self, s, words):
        res = []
        if len(s) == 0:
            return res
        dict_length = len(words)
        if dict_length == 0:
            return res
        word_length = len(words[0])
        start_index = 0

        # while start_index + (dict_length * word_length) <= len(s):
        #     temp_s = s[start_index : start_index + (dict_length * word_length)]
        #     for word in words:
        #         if word not in temp_s:
        #             break
        #         temp_s = temp_s[ : temp_s.index(word)] + temp_s[temp_s.index(word) + word_length : ]
        #     else:
        #         res.append(start_index)
        #     start_index += 1
        # return res
        while start_index + (dict_length * word_length) <= len(s):
            temp_s = s[start_index : start_index + (dict_length * word_length)]
            s_list = [temp_s[i:i+word_length] for i in range(0, len(temp_s), word_length)]
            for word in words:
                if word not in s_list:
                    break
                # s_list = s_list[:s_list.index(word)] + s_list[s_list.index(word) + word_length:]
                s_list.pop(s_list.index(word))
            else:
                res.append(start_index)
            start_index += 1
        return res

if __name__ == '__main__':
    s = Solution()
    S = "wordgoodgoodgoodbestword"
    words = ["word","good","best","word"]
    print(s.findSubstring(S, words))