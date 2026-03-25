from bisect import bisect_left
from typing import List

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        result = [] 
        prefix = ""

        for ch in searchWord: 
            prefix+=ch 
            i = bisect_left(products, prefix)

            suggestions = []
            for j in range(i, min(i+3, len(products))):
                if products[j].startswith(prefix): 
                    suggestions.append(products[j])
            
            result.append(suggestions)

        return result