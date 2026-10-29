class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        
        def get_count(s):
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            return count
        count1 = get_count(s1) # O(k)
        for i in range(len(s2) - k + 1): # O(n - k+1)
            substring = s2[i : i + k] # O(k)
            count2 = get_count(substring) # O(k)
            if count1 == count2: # O(k)
                return True
        return False
