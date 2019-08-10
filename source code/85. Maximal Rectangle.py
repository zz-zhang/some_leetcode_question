class Solution:
    def maximalRectangle(self, matrix) -> int:
        if not matrix or not matrix[0]:
            return 0
        matrix = [[int(item) for item in _] for _ in matrix]
        a = [[item for item in _] + [0] for _ in matrix]
        result = 0
        for i in range(1, len(a)):
            for j in range(0, len(a[i])):
                a[i][j] = a[i - 1][j] + a[i][j] if a[i][j] != 0 else a[i][j]
        # for i in range(0, len(a)):
        #     print(a[i])
        for line in a:
            stack = [-1]
            for i in range(0, len(line)):
                while line[i] < line[stack[-1]]:
                    h = line[stack[-1]]
                    stack.pop()
                    w = i - stack[-1] - 1

                    result = max(result, h * w)
                stack.append(i)
        return result

if __name__ == '__main__':
    sol = Solution()
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    # matrix = [['0', '1'],
    #           ['1', '1']]
    print(sol.maximalRectangle(matrix))
