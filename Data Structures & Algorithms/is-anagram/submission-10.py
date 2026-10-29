class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # hashmap 
        my_map1 = dict()
        my_map2 = dict()
        "racecar"
        for c in s:
            my_map1[c] = my_map1.get(c, 0) + 1
            # if c in my_map1:
            #     my_map1[c] += 1
            # else:
            #     my_map1[c] = 1

        for c in t:
            my_map2[c] = my_map2.get(c, 0) + 1
        
        if my_map1 == my_map2:
            return True
        return False