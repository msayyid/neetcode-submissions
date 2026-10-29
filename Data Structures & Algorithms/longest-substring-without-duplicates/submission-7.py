class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # using map 
        # the idea is to use a map of char : last_seen index
        # if char is in chars we update the value of it(the index)
        # and shrink our window (l += 1)
        chars = dict()
        l = 0
        max_length = 0
        for r in range(len(s)):
            if s[r] in chars:
                l = max(l, chars[s[r]] + 1)
            chars[s[r]] = r
            max_length = max(max_length, r - l + 1)
        return max_length

        
        
        # l = 0
        # max_length = 0
        # chars = set()
        # for r in range(len(s)):
        #     while s[r] in chars:
        #         chars.remove(s[l])
        #         l += 1

        #     chars.add(s[r])
        #     max_length = max(max_length, r - l + 1)
        # return max_length