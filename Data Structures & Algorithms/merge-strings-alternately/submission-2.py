class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        count = 0
        count1 = 0
        final = []
        for i in range(len(word1) + len(word2)):
            if i < len(word1):
                final.append(word1[i])
                # count += 1

            if i < len(word2):
                final.append(word2[i])
            # count += 1
            # count1 += 1
        return "".join(final)