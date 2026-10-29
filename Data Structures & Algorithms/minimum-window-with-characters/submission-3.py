class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        count_t = dict()
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1
        
        window = {}
        have = 0
        need = len(count_t)

        print(count_t)
        l = 0
        min_length = float("inf")
        boundaries = [-1, -1]
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in count_t and window[s[r]] == count_t[s[r]]:
                have += 1 # 

            # shrink window
            while have == need:
                if (r - l + 1) < min_length:
                    boundaries = [l, r]
                    min_length = r - l + 1
                
                window[s[l]] -= 1

                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                
                l += 1

        l, r = boundaries
        return s[l : r + 1] if min_length != float("inf") else ""
            

