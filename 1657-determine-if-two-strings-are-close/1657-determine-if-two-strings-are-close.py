class Solution:
    def closeStrings(self, w1: str, w2: str) -> bool:
        if len(w1) != len(w2): return False        
        from collections import Counter
        f1, f2 = Counter(w1), Counter(w2)        
        if set(f1.keys()) != set(f2.keys()): return False        
        return sorted(f1.values()) == sorted(f2.values())