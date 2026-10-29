class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        is_slash = False
        i = 0
        while i < len(path):
            if not stack or stack[-1] != "/":
                stack.append(path[i])
                # i += 1
            if stack and stack[-1] == "/" and (path[i].isalnum() or path[i] == "_"):
                stack.append(path[i])
                # i += 1
            i += 1
        print(stack)
        if len(stack) > 1 and stack[-1] == "/":
            stack.pop()
        return "".join(stack)





        # for c in path:
        #     if not stack and c == "/":
        #         stack.append("/")
        #     if stack[-1] == "/" or stack[-1].isalnum():
        #         if c != "." and c != "/":
        #             stack.append(c)
        #         if c == "/":
        #             stack.append(c)
        # print("".join(stack))