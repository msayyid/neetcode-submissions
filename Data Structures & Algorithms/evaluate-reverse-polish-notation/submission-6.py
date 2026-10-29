class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        total = 0
        stack = []
        # num1 = int(tokens[0])
        # num2 = int(tokens[1])
        # stack.append(num1)
        # stack.append(num2)
        for i in range(len(tokens)):
            
            if tokens[i] == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num1) + int(num2))
            elif tokens[i] == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 * num2)
            elif tokens[i] == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)
            elif tokens[i] == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num2 / num1))
            else:
                stack.append(int(tokens[i]))
        # print(stack)
        return stack[0]