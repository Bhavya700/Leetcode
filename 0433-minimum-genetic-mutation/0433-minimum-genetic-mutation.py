class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank=set(bank)
        if end not in bank:
            return -1
        queue = deque()
        queue.append((start, 0))
        visited={start}
        while queue:
            gene, level = queue.popleft()
            if gene==end:
                return level
            for i in range(len(gene)):
                for letter in "ACGT":
                    new = gene[:i] + letter + gene[i+1:]
                    if new not in visited and new in bank:
                        queue.append((new, level+1))
                        visited.add(new)
        return -1
