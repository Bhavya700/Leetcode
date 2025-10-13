class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        prev = {}
        l=0
        a=0
        while a<len(words):
            curr = dict(Counter(words[a]))
            if curr!=prev:
                prev=curr
                a+=1
            else:
                del words[a]

        return words