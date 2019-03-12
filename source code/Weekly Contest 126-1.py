

class Solution:
    def commonChars(self, A):
        dict = {chr(a) : 0 for a in range(97, 123)}
        min_dict = {chr(a) : 0x3f3f for a in range(97, 123)}
        alphabate = [chr(a) for a in range(97, 123)]
        length = len(A)
        res = []


        if length == 0:
            return res
        for word in A:
            temp_min_dict  = {chr(a) : 0 for a in range(97, 123)}
            for alpha in word:
                dict[alpha] += 1
                temp_min_dict[alpha] += 1
            for alpha in alphabate:
                min_dict[alpha] = min(min_dict[alpha], temp_min_dict[alpha])

        for item in dict:
            # print(alphabate[item])
            if dict[item] >= length:
                if min_dict[item] != 0:
                    for _ in range(0, min_dict[item]):
                        res.append(item)

        return res

if __name__ == '__main__':
    s = Solution()
    input = ["cool","lock","cook"]
    print(s.commonChars(input))
