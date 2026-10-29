class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        count = 0
        final = []
        for i in range(len(word1) + len(word2)):
            if count < len(word1):
                final.append(word1[i])
                # count += 1

            final.append(word2[i])
            count += 1
        return "".join(final)