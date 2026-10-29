class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        count_t = dict()
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        window = dict()
        have = 0 # to keep track of how many chars meet the requirement in the window
        need = len(t) # number of unique elements in t we need to match

        min_length = float("inf")
        result = [-1, -1] # to keep track of shortest valid window boundaries
        l = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1 # add the element to the window with incremeting its frequency
            if s[r] in count_t and window[s[r]] == count_t[s[r]]: # check if first the current element in window then if its count matches with the count of count_t's element's freq
                have += 1 # + one element fully meets the requirement (meaning it is in count_t and its freq is similar to count_t's)

            # shrink the window
            while have == need:
                # now we know that we have the elements in window that are in count_t
                # and now we need to check if we can get shorter window
                if r - l + 1 < min_length: # if the current window is shorter than the previous (still being a valid window)
                    # update the result list
                    result = [l, r]
                    min_length = r - l + 1

                window[s[l]] -= 1
                # check whether the shrinking decrements an element of the valid windw
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1 # have is decrement if our shrinking has affected the elements which are common in t and s
                l += 1
            
        return s[result[0] : result[1] + 1] if min_length != float("inf") else ""