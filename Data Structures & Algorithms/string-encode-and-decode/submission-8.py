class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        my_string = []

        for i in range(len(strs)):
            temp = strs[i]
            my_string.append(temp)
            if i < len(strs) - 1:
                my_string.append("#")
        # print("".join(my_string))
        return "".join(my_string)

    def decode(self, s: str) -> List[str]:
        if not s:
            return [""]
        my_list = []
        word = []

        i = 0
        while i < len(s):
            while i < len(s) and s[i] != "#":
                word.append(s[i])
                i += 1
            my_list.append("".join(word))
            word = []
            i += 1
        # print("my list is in here")
        # print(my_list)
        return my_list