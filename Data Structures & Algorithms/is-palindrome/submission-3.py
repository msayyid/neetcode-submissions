class Solution:
    def isPalindrome(self, s: str) -> bool:
        # # numbers = "01234567890"
        # # alph_nums = "abcdefghijklmnopqrstuvwxyz01234567890"
        # alph_nums = {
        #         'a','b','c','d','e','f','g','h','i','j','k','l','m',
        #         'n','o','p','q','r','s','t','u','v','w','x','y','z',
        #         '0','1','2','3','4','5','6','7','8','9','0'}
        # s_only = ""
        # for i in range(len(s)):
        #     if s[i].lower() in alph_nums:
        #         s_only += s[i].lower()
        # s_back = ""
        # for i in range(len(s_only) - 1, -1, -1):
        #     s_back += s_only[i]
        
        # if s_back == s_only:
        #     return True
        # return False
        # l, r = 0, len(s) - 1
        # while l < r:
        #     if 48 <= ord(s[l]) <= 57 and 48 <= ord(s[r]) <=57 or  65 <= ord(s[l]) <= 90 and 65 <= ord(s[r]) <=90 or 97 <= ord(s[l]) <= 122 and 97 <= ord(s[r]) <=122:
        #         if s[l] != s[r]:
        #             return False
        #     elif 
        #         l += 1
        #         r -= 1
        # return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l].isalnum() and s[r].isalnum():
                if s[l].lower() != s[r].lower():
                    return False
                r -= 1
                l += 1
            elif s[l].isalnum() and not s[r].isalnum():
                r -= 1
            elif not s[l].isalnum() and s[r].isalnum():
                l += 1
            else:
                r -= 1
                l += 1
        return True
