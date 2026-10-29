class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(s, l, r):
            return s[l:r+1] == s[l:r+1][::-1]
            # if s[l:r+1] == s[l:r+1][::-1]:
            #     return True
            # return False
        l, r = 0, len(s) - 1
        count = 0
        while l < r :
            if s[l] != s[r]:
                result = is_palindrome(s, l+1, r) or is_palindrome(s, l, r-1)
                return result
            l, r = l + 1, r - 1
        return True
        # while l <= r:
        #     if s[l] != s[r]:
        #         if s[l+1] != s[r] and l < r:
        #             if s[l] != s[r-1] and l < r:
        #                 return False
        #             else:
        #                 l += 1
        #                 r -= 2
        #                 count += 1
        #         else:
        #             l += 2
        #             r -= 1
        #             count += 1
        #     else:
        #         l += 1
        #         r -= 1
        # # if s[l-1] != s[r+1] and len(s) % 2 == 0:
        # #     return False
        # if count > 1: return False
        # return True