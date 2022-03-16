from random import shuffle


class Solution:
    def validateStackSequences(self, pushed, popped):
        stack = []
        i = 0
        j = 0
        while i < len(pushed):
            # print(stack)
            # breakpoint()
            while j < len(popped) and len(stack) > 0 and stack[-1] == popped[j]:
                stack = stack[:-1]
                j += 1
            stack.append(pushed[i])
            i += 1
        while j < len(popped) and len(stack) > 0 and stack[-1] == popped[j]:
            stack = stack[:-1]
            j += 1
        return len(stack) == 0

if __name__ == '__main__':
    sol = Solution()
    pushed = [i for i in range(1000)]
    popped = [i for i in pushed]
    shuffle(popped)
    print(len(pushed))
    print(pushed)
    print(popped)
    print(sol.validateStackSequences(pushed, popped))
        