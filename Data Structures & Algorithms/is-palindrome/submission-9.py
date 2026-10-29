class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alpha_num(s[l]):
                l += 1
            while l < r and not self.alpha_num(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def alpha_num(self, c):
        return (ord("A") <= ord(c) <= ord("Z") or
                ord("a") <= ord(c) <= ord("z") or
                ord("0") <= ord(c) <= ord("9")
                )
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
