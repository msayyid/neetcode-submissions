class Solution:
    def isValid(self, s: str) -> bool:
        parantheses = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }

        opening = {"(", "[", "{"}
        closing = {")", "]", "}"}

        stack = []
        for i in range(len(s)):
            if s[i] in opening:
                stack.append(s[i])
            # elif s[i] in closing:
            else:
                if stack and s[i] == parantheses[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return False if stack else True