class Solution:
    def isPalindrome(self, s: str) -> bool:
        # numbers = "01234567890"
        # alph_nums = "abcdefghijklmnopqrstuvwxyz01234567890"
        # alph_nums = {
        #         'a','b','c','d','e','f','g','h','i','j','k','l','m',
        #         'n','o','p','q','r','s','t','u','v','w','x','y','z',
        #         '0','1','2','3','4','5','6','7','8','9'}
        s_array = []
        # s_only = ""
        for i in range(len(s)):
            if s[i].isalnum():
            # if s[i].lower() in alph_nums:
                s_array.append(s[i].lower())
        # s_only = "".join(s_array)

        # s_b_array = []
        # # s_back = ""
        # for i in range(len(s_array) - 1, -1, -1):
        #     s_b_array.append(s_array[i])
        return s_array == s_array[::-1]
        
        
        # if s_array == s_b_array:
        #     return True
        # return False

        # l, r = 0, len(s) - 1
        # while l < r:
        #     if s[l].isalnum() and s[r].isalnum():
        #         if s[l].lower() != s[r].lower():
        #             return False
        #         r -= 1
        #         l += 1
        #     elif s[l].isalnum() and not s[r].isalnum():
        #         r -= 1
        #     elif not s[l].isalnum() and s[r].isalnum():
        #         l += 1
        #     else:
        #         r -= 1
        #         l += 1
        # return True
