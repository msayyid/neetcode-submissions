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
        # print("".join(my_string))
        return "".join(my_string)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        my_list = []
        word = []

        i = 0
        while i < len(s):
            if start:
                j = 0
                length = int(s[i])
                if length == 0:
                    return [""]
                i += 1
                while j < length:
                    word.append(s[i])
                    j += 1
                    i += 1
                my_list.append("".join(word))
                word = []
                i += 1
        # print(my_list)
        return my_list