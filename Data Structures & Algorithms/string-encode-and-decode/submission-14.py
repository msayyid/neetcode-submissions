class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        my_string = []

        for i in range(len(strs)):
            temp = strs[i]
            my_string.append(str(len(temp)))
            my_string.append("#")
            my_string.append(temp)
        return "".join(my_string)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        my_list = []
        word = []

        i = 0
        length = []
        while i < len(s):
            j = 0
            while i < len(s) and s[i] != "#":
                length.append(s[i])
                i += 1
            length = int("".join(length))
            i += 1
            while j < length:
                word.append(s[i])
                j += 1
                i += 1
            my_list.append("".join(word))
            word = []
            length = []
        return my_list