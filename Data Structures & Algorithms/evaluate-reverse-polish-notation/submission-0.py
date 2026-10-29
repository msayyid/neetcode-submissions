class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        total = 0
        stack = []
        num1 = int(tokens[0])
        num2 = int(tokens[1])
        stack.append(num1)
        stack.append(num2)
        for i in range(2, len(tokens)):
            if tokens[i] == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif tokens[i] == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif tokens[i] == "-":
                stack.append(int(stack.pop()) - int(stack.pop()))
            elif tokens[i] == "/":
                stack.append(int(stack.pop()) / int(stack.pop()))
            else:
                stack.append(tokens[i])
        print(stack)
        return stack[-1]