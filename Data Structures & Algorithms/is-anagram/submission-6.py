class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        my_map = dict()
        for i in range(len(s)):
            my_map[s[i]] = my_map.get(s[i], 0) + 1

        for c in t:
            if c not in my_map:
                return False
            my_map[c] -= 1
        
        # return True if sorted(s) == sorted(t) else False

        