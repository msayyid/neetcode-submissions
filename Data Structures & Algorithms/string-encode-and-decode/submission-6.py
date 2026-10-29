class Solution:

    def encode(self, strs: List[str]) -> str:
        # the idea is to encode using the length of a string in a list
        # with a symbol, which we do not add to the actual word when decoding
        # i will use length + # + str
        # full_string = ""
        return "".join(f"{len(s)}#{s}" for s in strs)
        # for s in strs:


        #     full_string += str(len(s))
        #     "#".join(s)
        #     # full_string += "#"
        #     # full_string += s
        # return full_string



    def decode(self, s: str) -> List[str]:
        result = []
        # when decoding, we extract the numbers up to #
        # typecast it, and run this number of times to jump and to build the string
        ptr = 0
        start = 0
        while ptr < len(s):
            if s[ptr] == "#":
                # number_rep = 
                temp_str = s[ptr+1:ptr+int(s[start:ptr])+1]
                result.append(temp_str)
                ptr += int(s[start:ptr]) + 1
                start = ptr
            else: 
                ptr += 1
        return result
        

