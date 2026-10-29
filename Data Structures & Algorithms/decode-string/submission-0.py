class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        string = []
        k = ""

        for c in s:
            if c.isdigit():
                k += c

            elif c == "[":
                stack.append((string, int(k)))
                string = []
                k = ""

            elif c == "]":
                prev_string, repeat = stack.pop()
                string = prev_string + string * repeat

            else:
                string.append(c)
        return "".join(string)