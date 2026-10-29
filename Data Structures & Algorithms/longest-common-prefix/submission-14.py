class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for c in range(len(strs[0])):
            for i in range(len(strs)):
                if strs[i] == "":
                    return ""
                if c == len(strs[i]) or strs[0][c] != strs[i][c]:
                    return strs[0][:c]
        return strs[0]