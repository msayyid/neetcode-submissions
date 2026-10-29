class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        count_t = {}
        window = {}
        
        # fix the t counter
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        have = 0
        need = len(count_t)
        l = 0
        result = [-1, -1]
        min_length = float("inf")

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in count_t and window[c] == count_t[c]:
                have += 1

            while have == need:
                min_length = min(min_length, r - l + 1)
                result = [l, r]

                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1

        l, r = result
        return s[l:r+1]