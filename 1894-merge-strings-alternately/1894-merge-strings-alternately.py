class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        l = min(len(word1),len(word2))
        for i in range(l):
            output += word1[i] + word2[i]
        output += word1[l:] + word2[l:]
        return output