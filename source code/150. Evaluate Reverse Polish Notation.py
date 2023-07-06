from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operation_dict = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: int(x / y)}
        stack = []
        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                res = operation_dict[token](num1, num2)
                stack.append(res)
        #     print(token)
        #     print(stack)
        #     breakpoint()
        # print(stack)
        return stack.pop()

if __name__ == '__main__':
    sol = Solution()
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(sol.evalRPN(tokens))