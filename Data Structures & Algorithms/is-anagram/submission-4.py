class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        my_map = dict()
        for i in range(len(s)):
            my_map[s[i]] = my_map.get(s[i], 0) + 1

        for i in range(len(t)):
            if t[i] in my_map:
                my_map[t[i]] -= 1
            else: return False
        
        for k, v in my_map.items():
            if v != 0:
                return False
        return True
        # return True if sorted(s) == sorted(t) else False

        