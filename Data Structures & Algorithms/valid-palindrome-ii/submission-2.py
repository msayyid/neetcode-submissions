class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        count = 0
        while l <= r:
            if s[l] != s[r]:
                if s[l+1] != s[r] and l < r:
                    if s[l] != s[r-1] and l < r:
                        return False
                    else:
                        l += 1
                        r -= 2
                else:
                    l += 1
                    r -= 1
            l += 1
            r -= 1
        return True