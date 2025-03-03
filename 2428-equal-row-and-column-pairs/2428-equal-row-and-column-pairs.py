class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        transpose=Counter(zip(*grid))
        grid=Counter(map(tuple,grid))
        return sum(transpose[a]*grid[a] for a in transpose)