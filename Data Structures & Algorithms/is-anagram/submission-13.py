class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        my_map = dict()

        for i in range(len(s)):
            my_map[s[i]] = my_map.get(s[i], 0) + 1
            my_map[t[i]] = my_map.get(t[i], 0) - 1
        
        for value in my_map.values():
            if value != 0:
                return False
        return True