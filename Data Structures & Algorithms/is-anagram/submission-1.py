class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # my_map = defaultdict()
        # for i in range(len(s)):
        #     if s[i] not in my_map:
        #         my_map[s[i]] += 1
        #     if t[i] in my_map:
        #         my_map[s[t]] -= 1

        # s.sort()
        # t.sort()
        return True if sorted(s) == sorted(t) else False

        