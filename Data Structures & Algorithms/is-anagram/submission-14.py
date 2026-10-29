class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26
        for i in range(len(s)):
            count[s[i]] += 1
            count[t[i]] -=1 

        for v in count:
            if v != 0:
                return False
        return True
        