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
                        count += 1
                else:
                    l += 2
                    r -= 1
                    count += 1
            else:
                l += 1
                r -= 1
        # if s[l-1] != s[r+1] and len(s) % 2 == 0:
        #     return False
        if count > 1: return False
        return True