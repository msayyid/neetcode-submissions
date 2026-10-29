class Solution:

    def encode(self, strs: List[str]) -> str:
        my_string = ""
        if strs:
            for i in range(len(strs)):
                my_string += strs[i]
                my_string += "|"
            return my_string
        return my_string

    def decode(self, s: str) -> List[str]:
        my_list = []
        temp_str = ""
        if s:
            for i in range(len(s)):
                temp_str += s[i]
                if s[i] == "|":
                    my_list.append(temp_str[:-1:])
                    temp_str = ""
            
            # for i in range(len(s)):
            #     if s[i] != "|":
            #         temp_str += s[i]
            #     my_list.append(temp_str)
            #     temp_str = ""

            return my_list
        return my_list


