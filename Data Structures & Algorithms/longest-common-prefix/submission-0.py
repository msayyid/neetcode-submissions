class Solution:
    def longestCommonPrefix(self, strs) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            for j in range(min(len(prefix), len(strs[i]))):
                if prefix[j] == strs[i][j]:
                    continue
                else:
                    prefix = strs[i][:j]
                    break
            # if the prefix is longer and we do not enter the else
            # inside the inner loop, then check and assign the shorter to prefix
            if len(prefix) > len(strs[i]):
                prefix = strs[i]
        return prefix