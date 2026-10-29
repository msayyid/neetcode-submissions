class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        my_map = dict()

        for i in range(len(s)):
            if s[i] in my_map:
                my_map[s[i]] += 1
            else:
                my_map[s[i]] = 1
            
            if t[i] in my_map:
                my_map[t[i]] -= 1
            else:
                my_map[t[i]] = -1
        
        for value in my_map.values():
            if value != 0:
                return False
        return True