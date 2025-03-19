class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            dict[key].append(s)
        
        return list(dict.values())