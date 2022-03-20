class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occ = {chr(n + ord('a')):-1 for n in range(26)}
        for idx, char in enumerate(s):
            last_occ[char] = idx
        # print(last_occ)

        stack = []
        stack_recoder = {chr(n + ord('a')):False for n in range(26)}
        for idx, char in enumerate(s):
            # breakpoint()
            if not stack_recoder[char]:
                while len(stack) > 0 and stack[-1] > char and last_occ[stack[-1]] > idx:
                    stack_recoder[stack[-1]] = False
                    stack = stack[:-1]
                stack.append(char)
                stack_recoder[char] = True
                # print(stack)

        # print(stack)
        return ''.join(stack)


if __name__ == '__main__':
    from random import randint
    sol = Solution()
    # s = ''.join([chr(randint(ord('a'), ord('z'))) for _ in range(100)])
    # print(s)
    s = "bcabc"
    print(sol.removeDuplicateLetters(s))