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
        # word = []
        word_str = ""

        i = 0
        length = []
        length_str = ""
        while i < len(s):
            j = 0
            while i < len(s) and s[i] != "#":
                # length.append(s[i])
                length_str += s[i]
                i += 1
            # length = int("".join(length))
            length_str = int(length_str)
            i += 1
            # while j < length:
            while j < int(length_str):
                # word.append(s[i])
                word_str += s[i]
                j += 1
                i += 1
            # my_list.append("".join(word))
            my_list.append(word_str)
            # word = []
            word_str = ""
            # length = []
            length_str = ""
        return my_list