class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for o in operations:
            if o == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 + num2)
                # stack.append(stack[-1] + stack[-2])
            elif o == "D":
                stack.append(stack[-1] * 2)
            elif o == "C":
                stack.pop()
            else:
                stack.append(int(o))
        return sum(stack)