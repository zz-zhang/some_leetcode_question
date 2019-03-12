class Solution:

    # def flip_length(self, input, flag):
    #     flag = 0
    #     max_length = 0
    #     for i in range(0, len(input)):
    #         if input[i] == 0:
    #             input[i] = 1
    #             length = 1
    #             end = i + 1
    #             start = i - 1
    #             if start >= 0:
    #                 while start >= 0 and input[start] != 0:
    #                     start -= 1
    #                     length += 1
    #             if end < len(input):
    #                 while end < len(input) and input[end] != 0:
    #                     if end < len(input) and input[end] != 0:
    #                         end += 1
    #                         length += 1
    #
    #             input[i] = 0
    #             if length > max_length:
    #                 max_length = length
    #                 flag = i
    #     return max_length, flag
    def calc_coun(self, A, flag):
        aim = A[flag]
        length = 1
        end = flag + 1
        # start = flag - 1
        # if start >= 0:
        #     while start >= 0 and A[start] == aim:
        #         start -= 1
        #         length += 1
        # if end < len(A):
        while end < len(A) and A[end] == aim:
            end += 1
            length += 1
        return length

    def longestOnes(self, A, K):
        start_with = A[0]
        conu_length = []
        i = 0
        while i < len(A):
        # for i in range(0, len(A) - 1):
            if i > 0:
                while A[i] == A[i - 1]:
                    i += 1
                    if i >= len(A):
                        break
            if i >= len(A):
               break
            length = self.calc_coun(A, i)
            conu_length.append(length)
            i += 1
        print(conu_length)

        if start_with == 1:

        # if K == 0:
        #     max_length = 0
        #     for i in range(0, len(A)):
        #         if A[i] == 1:
        #             length = 1
        #             end = i + 1
        #             start = i - 1
        #             if start >= 0:
        #                 while start >= 0 and A[start] != 0:
        #                     start -= 1
        #                     length += 1
        #             if end < len(A):
        #                 while end < len(A) and A[end] != 0:
        #                     if end < len(A) and A[end] != 0:
        #                         end += 1
        #                         length += 1
        #             if length > max_length:
        #                 max_length = length
        #     return max_length
        #
        # bag = [0 for _ in range(0, K + 1)]
        # for i in range(1, K + 1):
        #     length, flag = self.flip_length(A)
        #     bag[i] = max(bag[i - 1], length)
        #     A[flag] = 1
        # # print(A)
        # return bag[K]

if __name__ == '__main__':
    s = Solution()
    A = [1,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,0,0,1,1,0,1,1]
    test = [1,1,1,0,0,0,1]
    K = 8

    print(s.longestOnes(A, K))