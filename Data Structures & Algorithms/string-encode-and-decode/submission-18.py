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
        word_str = ""

        i = 0
        length = []
        while i < len(s):
            j = 0
            while i < len(s) and s[i] != "#":
                length.append(s[i])
                i += 1
            i += 1
            length = int("".join(length))
            word_str = s[i:i + length]
            
            i += length
            my_list.append(word_str)
            word_str = ""
            length = []
        return my_list