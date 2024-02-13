class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operands = set("+", "-", "*", "/")
        for token in tokens:
            if token in operands:
                b = stack.pop()
                a = stack.pop()
                match token:
                    case "+":
                        val = a + b
                    case "-":
                        val = a - b
                    case "*":
                        val = a * b
                    case "/":
                        val = int(a / b)
                stack.append(val)
            else:
                stack.append(int(token))
            # print(stack)
        return stack.pop()


s = Solution()
# print(s.evalRPN(["2", "1", "+", "3", "*"]))
print(s.evalRPN(["4", "13", "5", "/", "+"]))
print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
