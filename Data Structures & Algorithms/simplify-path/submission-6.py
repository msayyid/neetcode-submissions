class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""
        for c in path:
            if c == "/":
                # check if cur word is "..", if yes pop
                if cur == "..":
                    if stack: stack.pop()
                # if cur is not empty and cur is not a "." => append it
                elif cur != "" and cur != ".":
                    stack.append(cur)
                # and when c is "/", we stop building the word (or directory)
                cur = ""
            # build cur if c is not a "/"
            else:
                cur += c

        print(stack)
        # our stack now contains only the names of dirs so we need to make it a path
        return "/" + "/".join(stack)