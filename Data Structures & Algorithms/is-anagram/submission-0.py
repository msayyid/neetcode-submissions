class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_map = dict()
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in my_map:
                my_map[s[i]] = 1
            else: my_map[s[i]] += 1
        
        for j in range(len(t)):
            if t[j] not in my_map:
                return False
            else: my_map[t[j]] -= 1
        
        # for v in my_map.values():
        #     return False if v != 0 else True
        return all(v == 0 for v in my_map.values())
        