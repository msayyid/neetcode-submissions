class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return len(s)
        my_set = set()
        left = 0
        right = 0
        # my_set.add(s[left])
        length = 0
        max_length = 0
        while right < len(s):
            while left < right and s[right] in my_set:
                my_set.remove(s[left])
                left += 1
                length -= 1
            my_set.add(s[right])
            length += 1
            max_length = max(max_length, length)
            right += 1
        # print(my_set)
        # print(max_length)
        return max_length