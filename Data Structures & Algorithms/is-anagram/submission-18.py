class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mymap = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            mymap[s[i]] = mymap.get(s[i], 0) + 1
            mymap[t[i]] = mymap.get(t[i], 0) - 1

        for val in mymap.values():
            if val != 0: 
                return False

        return True