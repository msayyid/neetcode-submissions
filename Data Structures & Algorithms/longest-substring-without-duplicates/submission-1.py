class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l = 0 
        res = 0
        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            res = max(res, r - l + 1)
        return res
            
        # res = 0
        # for i in range(len(s)):
        #     charSet = set()
        #     for j in range(i, len(s)):
        #         if s[j] in charSet:
        #             break
        #         charSet.add(s[j])
        #     res = max(res, len(charSet))
        # return res