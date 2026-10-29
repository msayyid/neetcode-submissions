class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # the idea would be to create a count hashmap
        # that has the frequency of each letter
        count = {}
        max_length = 0 
        # max_length is needed to keep record of the longest valid 
        # substring length that can be made into one letter string
        max_freq = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_freq = max(count[s[r]], max_freq)
            window_length = r - l + 1
            diff = window_length - max_freq
            if diff > k:
                count[s[l]] -= 1
                l += 1
            max_length = max(max_length, r - l + 1)
        return max_length

