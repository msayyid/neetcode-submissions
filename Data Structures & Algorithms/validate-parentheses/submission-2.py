class Solution:
    def isValid(self, s: str) -> bool:
        parantheses = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        # opening = {"(", "[", "{"}
        # closing = {")", "]", "}"}

        stack = []
        for c in s:
            if c in parantheses and stack:
                if stack[-1] == parantheses[c]:
                    stack.pop()
                else:
                    return False
            else: # it is opening bracket now
                stack.append(c)
        return False if stack else True