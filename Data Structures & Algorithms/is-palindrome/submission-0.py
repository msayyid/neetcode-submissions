class Solution:
    def isPalindrome(self, s: str) -> bool:
        # numbers = "01234567890"
        alph_nums = "abcdefghijklmnopqrstuvwxyz01234567890"
        l = 0
        r = len(s) - 1
        s_only = ""
        for i in range(len(s)):
            if s[i].lower() in alph_nums:
                s_only += s[i].lower()
        s_back = ""
        for i in range(len(s_only) - 1, -1, -1):
            s_back += s_only[i]
        print(s_only)
        print(s_back)
        
        if s_back == s_only:
            return True
        return False