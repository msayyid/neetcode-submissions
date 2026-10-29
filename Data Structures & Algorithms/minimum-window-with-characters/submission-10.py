class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        count = dict()
        for c in t:
            count[c] = count.get(c, 0) + 1

        print(count)

        window = dict()
        have = 0
        need = len(count)
        min_length = float("inf")
        result = [-1, -1]

        l = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1

            if s[r] in count and window[s[r]] == count[s[r]]:
                have += 1

            while have == need:
                # update shortest window boundary
                if min_length > r - l + 1:
                    result = [l, r]
                    min_length = r - l + 1
                
                window[s[l]] -= 1
                
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1
                l += 1

        l, r = result
        return s[l : r + 1] if min_length != float("inf") else ""
