class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() == s[right].lower():
                    left += 1
                    right -= 1
                else:
                    return False

            elif left < right and not s[left].isalnum() and s[right].isalnum():
                left += 1
            
            elif left < right and s[left].isalnum() and not s[right].isalnum():
                right -= 1
            
            else:
                left += 1
                right -= 1
            
        return True